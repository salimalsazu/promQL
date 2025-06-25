import psutil
import asyncio
from prometheus_client import Gauge

# Define Gauges as None initially
cpu_usage_gauge = None
memory_rss_gauge = None
memory_vms_gauge = None
thread_count_gauge = None

def get_metrics():
    global cpu_usage_gauge, memory_rss_gauge, memory_vms_gauge, thread_count_gauge
    if cpu_usage_gauge is None:
        cpu_usage_gauge = Gauge('process_cpu_percent', 'CPU usage percent')
    if memory_rss_gauge is None:
        memory_rss_gauge = Gauge('process_resident_memory_bytes', 'Resident memory bytes used')
    if memory_vms_gauge is None:
        memory_vms_gauge = Gauge('process_virtual_memory_bytes', 'Virtual memory bytes used')
    if thread_count_gauge is None:
        thread_count_gauge = Gauge('process_thread_count', 'Number of threads')
    return cpu_usage_gauge, memory_rss_gauge, memory_vms_gauge, thread_count_gauge

async def collect_system_metrics_periodically(interval: int = 5):
    cpu_usage, mem_rss, mem_vms, threads = get_metrics()
    while True:
        cpu_percent = psutil.cpu_percent()
        mem_info = psutil.Process().memory_info()
        thread_count = psutil.Process().num_threads()

        cpu_usage.set(cpu_percent)
        mem_rss.set(mem_info.rss)
        mem_vms.set(mem_info.vms)
        threads.set(thread_count)

        await asyncio.sleep(interval)
