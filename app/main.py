from fastapi import FastAPI
from app.routers import api, health
from app.middleware.metrics_middleware import MetricsMiddleware
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
import asyncio
from app.metrics import system_metrics

app = FastAPI()

# Add Metrics Middleware to track HTTP metrics
app.add_middleware(MetricsMiddleware)

# Include routers
app.include_router(api.router)
app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "FastAPI Metrics Monitoring System is running"}

@app.get("/metrics")
async def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

# Background task to collect system metrics every 5 seconds
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(system_metrics.collect_system_metrics_periodically())


