import os
import time

from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, Gauge, Histogram, generate_latest
from starlette.responses import Response

app = FastAPI(
    title="SRE Incident Simulator",
    version="1.0.0",
)

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total API requests",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "api_request_duration_seconds",
    "API request latency",
    ["endpoint"],
)

ACTIVE_REQUESTS = Gauge(
    "api_active_requests",
    "Number of active requests",
)

INCIDENT_MODE = Gauge(
    "incident_mode",
    "Current incident simulation mode",
    ["mode"],
)


def current_mode():
    return os.getenv("INCIDENT_MODE", "normal").lower()


@app.get("/")
def root():
    return {
        "service": "sre-incident-simulator",
        "status": "running",
        "incident_mode": current_mode(),
    }


@app.get("/health")
def health():
    mode = current_mode()

    if mode == "service_down":
        raise HTTPException(
            status_code=503,
            detail="Simulated service outage",
        )

    return {
        "status": "healthy",
        "incident_mode": mode,
    }


@app.get("/api/orders")
def orders():
    start = time.perf_counter()
    ACTIVE_REQUESTS.inc()

    try:
        mode = current_mode()

        if mode == "high_latency":
            time.sleep(2)

        if mode == "http_500":
            raise HTTPException(
                status_code=500,
                detail="Simulated internal server error",
            )

        return {
            "orders": [
                {"id": 1001, "status": "completed"},
                {"id": 1002, "status": "processing"},
            ],
            "incident_mode": mode,
        }

    finally:
        elapsed = time.perf_counter() - start

        REQUEST_LATENCY.labels(
            endpoint="/api/orders"
        ).observe(elapsed)

        ACTIVE_REQUESTS.dec()


@app.get("/metrics")
def metrics():

    INCIDENT_MODE.labels(
        mode=current_mode()
    ).set(1)

    return Response(
        generate_latest(),
        media_type="text/plain",
    )