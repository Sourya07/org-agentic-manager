import requests
import os
from dotenv import load_dotenv

load_dotenv()

PROMETHEUS_URL = os.getenv("PROMETHEUS_URL")

if not PROMETHEUS_URL:
    raise ValueError("PROMETHEUS_URL not set in .env")


def fetch_pod_metrics(pod_id: str):
    try:
        # CPU Query
        cpu_query = f'rate(container_cpu_usage_seconds_total{{pod="{pod_id}"}}[1m])'
        cpu_res = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={"query": cpu_query}).json()

        cpu_value = 0
        if cpu_res["data"]["result"]:
            cpu_value = float(cpu_res["data"]["result"][0]["value"][1])

        # MEMORY Query
        mem_query = f'container_memory_usage_bytes{{pod="{pod_id}"}}'
        mem_res = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={"query": mem_query}).json()

        mem_value = 0
        if mem_res["data"]["result"]:
            mem_value = float(mem_res["data"]["result"][0]["value"][1])

        return {
            "cpu": cpu_value,
            "memory": mem_value
        }

    except Exception as e:
        return {
            "cpu": 0,
            "memory": 0,
            "error": str(e)
        }