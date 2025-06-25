# FastAPI Metrics Monitoring System

## Overview

This project implements a FastAPI application with system-level and HTTP request metrics, exposed in Prometheus format.

## How to run

1. Build and run with Docker Compose:

   ```
   docker-compose up --build -d
   ```

2. Access endpoints:
   - Root: http://localhost:8000/
   - Health: http://localhost:8000/health
   - Metrics: http://localhost:8000/metrics
   - POST data: http://localhost:8000/data (POST JSON payload)
   - GET data: http://localhost:8000/data

## Prometheus Dashboard Access

- URL: http://localhost:9090

## Monitoring

- Prometheus can scrape metrics from `/metrics`
- System metrics collected using `psutil`
- HTTP request metrics collected via middleware

## Configuration

- Modify `app/config.py` to change intervals or histogram buckets.
