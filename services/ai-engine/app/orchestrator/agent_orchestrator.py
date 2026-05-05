from typing import List
from app.services.metrics_service import fetch_pod_metrics
from app.agents.cpu_agent import analyze_cpu
from app.agents.memory_agent import analyze_memory
from app.models.response_model import Insight


def run_analysis(pod_id: str):
    
    print(f"\n Analyzing pod: {pod_id}")

    metrics = fetch_pod_metrics(pod_id)

    print(f" Metrics received: {metrics}")

    insights = []

    if "cpu" in metrics:
        insights.extend(analyze_cpu(metrics["cpu"], pod_id))

    if "memory" in metrics:
        insights.extend(analyze_memory(metrics["memory"], pod_id))

    print(f" Insights generated: {insights}")

    return insights