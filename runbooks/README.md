# Runbooks

This folder contains operational runbooks for responding to incidents.

## Standard incident flow

1. Acknowledge the alert.
2. Verify the service status and impact.
3. Confirm whether the issue is a simulated or production incident.
4. Apply the identified mitigation.
5. Monitor recovery and record evidence.
6. Document the incident in a postmortem.

## Example runbook

### Service outage

- Check application health endpoint.
- Confirm the current incident mode.
- Validate the service dependency chain.
- Restart or recover the affected component if needed.
- Notify stakeholders and capture timeline notes.
