import time
import threading
import prometheus_client as prom
from flask import Flask

app = Flask(__name__)

REQUEST_COUNT = prom.Counter("app_requests_total", "Total number of requests")
REQUEST_LATENCY = prom.Summary("app_request_latency_seconds", "Request latency")


@app.route("/")
@REQUEST_LATENCY.time()
def index():
    REQUEST_COUNT.inc()
    return ("OK", 200)


@app.route("/stress")
@app.route("/stress/<int:duration>")
def stress_cpu(duration=30):
    REQUEST_COUNT.inc()

    # stress duration guardrail
    duration = min(duration, 120)

    def burn_cpu():
        end = time.time() + duration
        counter = 0
        while time.time() < end:
            counter = (counter + 1) % 1000000
            _ = counter**2

    # Use 2-3 threads max to avoid overwhelming the system
    num_threads = min(3, threading.active_count() + 2)
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=burn_cpu)
        thread.daemon = True
        thread.start()
        threads.append(thread)

    return f"CPU stress triggered: {num_threads} threads for {duration}s", 200


@app.route("/metrics")
def metrics():
    return prom.generate_latest(), 200, {"Content-type": "text/plain; charset=utf-8"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
