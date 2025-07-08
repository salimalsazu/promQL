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
   - UPDATE data: http://localhost:8000/data/{id}
   - DELETE data: http://localhost:8000/data/{id}

## Prometheus Dashboard Access

- URL: http://localhost:9090

## Monitoring

- Prometheus can scrape metrics from `/metrics`
- System metrics collected using `psutil`
- HTTP request metrics collected via middleware

## Configuration

- Modify `app/config.py` to change intervals or histogram buckets.

## System Metrics:

- process_cpu_percent - CPU usage (%)
- process_resident_memory_bytes - Physical memory in use (RSS)
- process_virtual_memory_bytes - Virtual memory size (VMS)
- process_thread_count - Active thread count

## HTTP Metrics

- http_requests_total - Count of all HTTP requests
- http_request_duration_seconds - Duration of each request (histogram)

## Data Endpoint Testing (via Postman)

### 1. POST /data

**URL:**
POST http://localhost:8000/data

**Example JSON Body:**
{
"id": "my-custom-id-001",
"name": "tafsir",
"age": 5,
"email": "salim@example.com"
}

> If you don’t provide an "id", the server will automatically generate a UUID.

**Example Response:**
{
"message": "Data stored",
"item": {
"id": "my-custom-id-001",
"name": "tafsir",
"age": 5,
"email": "salim@example.com"
},
"current_count": 1
}

### 2. GET /data

**URL:**
GET http://localhost:8000/data

**Response:**
{
"data": [
{
"id": "my-custom-id-001",
"name": "tafsir",
"age": 5,
"email": "salim@example.com"
}
]
}

### 3. PATCH /data/{id}

**URL:**
PATCH http://localhost:8000/data/my-custom-id-001

**Example JSON Body:**
{
"age": 6,
"email": "tafsir@example.com"
}

**Example Response:**
{
"message": "Item updated",
"item": {
"id": "my-custom-id-001",
"name": "tafsir",
"age": 6,
"email": "tafsir@example.com"
}
}

### 4. DELETE /data/{id}

**URL:**
DELETE http://localhost:8000/data/my-custom-id-001

**Example Response:**
{
"message": "Item deleted",
"item": {
"id": "my-custom-id-001",
"name": "tafsir",
"age": 6,
"email": "tafsir@example.com"
}
}
