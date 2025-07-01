# incident-sandbox

This project simulates a simple SRE environment with basic monitoring and alerting.

It includes a minimal Flask app that generates controlled CPU load.
The system is monitored using Prometheus and Node Exporter, with alerts routed through Alertmanager to Slack.

## Purpose

This is a self-contained portfolio project demonstrating:

- Building a minimal observability stack in Docker
- Defining metrics and alert rules in Prometheus
- Simulating and detecting system resource usage
- Sending alerts via Alertmanager + Slack integration

This project is not intended for production use.

## Stack

- Python (Flask)
- Docker & Docker Compose
- Prometheus
- Node Exporter
- Alertmanager
- Grafana (optional; dashboard not yet included)
- Slack (incoming webhook for alert delivery)

## License

MIT
