# SRE Incident Management

A lightweight incident simulation and operations training repository for practicing SRE workflows, service failure modes, and monitoring responses.

## Overview

This project contains a small FastAPI service that simulates operational incidents such as:

- service outage
- high latency
- internal server errors
- metric exposure for monitoring and alerting exercises

The repo is organized to support incident response runbooks, dashboards, monitoring configuration, and postmortem documentation.

## Repository structure

- `app/` - FastAPI application and tests
- `dashboards/` - dashboard definitions and screenshots
- `docs/` - supporting documentation
- `incidents/` - incident scenarios and examples
- `monitoring/` - Prometheus and Alertmanager configuration
- `postmortems/` - postmortem templates and completed examples
- `runbooks/` - operational response procedures
- `scripts/` - utility scripts and automation

## Architecture

The repository follows a simple SRE training workflow:

1. Service behavior is simulated by the FastAPI app in `app/main.py`.
2. Monitoring and alerting are represented in the `monitoring/` configuration.
3. Incident scenarios live in `incidents/` and are tied to response playbooks in `runbooks/`.
4. Post-incident learning is captured in `postmortems/`.
5. Dashboards and visualizations help the team review service health and incident impact.

## Example incident drill workflow

A common exercise for this project is:

1. Set the service to a failure mode.
2. Trigger alerts or observe degraded metrics.
3. Use the health endpoint and Prometheus output to confirm impact.
4. Follow the relevant runbook for mitigation.
5. Record the outcome in a postmortem.

Example:

```powershell
$env:INCIDENT_MODE = "service_down"
uvicorn app.main:app --reload
```

Then check:

- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/metrics

## Application endpoints

The service exposes the following routes:

- `GET /` - service metadata and current incident mode
- `GET /health` - health check endpoint
- `GET /api/orders` - simulated order data with configurable failure states
- `GET /metrics` - Prometheus metrics output

## Incident modes

The app reads the `INCIDENT_MODE` environment variable and supports these modes:

- `normal`
- `high_latency`
- `http_500`
- `service_down`

Example:

```powershell
$env:INCIDENT_MODE = "high_latency"
```

## Local setup

1. Open a terminal in the project root.
2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r app\requirements.txt
```

4. Run the API:

```powershell
uvicorn app.main:app --reload
```

5. Access the API locally:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/metrics

## Running tests

From the project root:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Monitoring

This repository includes monitoring configuration for:

- Prometheus
- Alertmanager

Use these resources to simulate alerting and response workflows during incident exercises.

## Notes

This repository is intended for training, simulations, and operational practice. It can be extended with additional incident scenarios, dashboards, playbooks, and automation.
