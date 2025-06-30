FROM python:3.12-alpine

WORKDIR /app

COPY app.py .
RUN pip install --no-cache-dir flask==3.1.1 prometheus_client==0.22.1

EXPOSE 5000 8000

CMD ["python", "app.py"]
