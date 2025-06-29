# incident-sandbox

This project simulates a simple SRE environment focused on monitoring, alerting, and incident response.

It includes a basic Flask web app that can trigger high CPU usage, monitored by Prometheus and visualized with Grafana. Alerts are sent through Alertmanager to Slack.

## Purpose

The goal is to demonstrate a practical understanding of core SRE concepts:
- Building a basic observability stack
- Defining metrics and alert rules
- Simulating and detecting incidents
- Responding and improving based on alert feedback

This is a learning and portfolio project, not intended for production use.

## Stack

- Python (Flask)
- Docker, Docker Compose
- Prometheus, Node Exporter
- Alertmanager
- Grafana
- Slack (for alert notifications)

## License

MIT License

