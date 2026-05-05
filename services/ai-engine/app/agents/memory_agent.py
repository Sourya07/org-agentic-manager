from typing import List
from app.models.response_model import Insight


MEMORY_HIGH_THRESHOLD = 0.8
MEMORY_MEDIUM_THRESHOLD = 0.6


def analyze_memory(memory_usage: float, pod_id: str) -> List[Insight]:
    insights: List[Insight] = []

    if memory_usage >= MEMORY_HIGH_THRESHOLD:
        insights.append(
            Insight(
                severity="CRITICAL",
                metric="MEMORY",
                reason=f"Memory utilization for pod '{pod_id}' exceeded threshold ({memory_usage:.2f})",
                recommendation="Check for memory leaks or increase resource limits"
            )
        )

    elif memory_usage >= MEMORY_MEDIUM_THRESHOLD:
        insights.append(
            Insight(
                severity="WARNING",
                metric="MEMORY",
                reason=f"Memory utilization for pod '{pod_id}' is above normal range ({memory_usage:.2f})",
                recommendation="Monitor usage trends and optimize memory allocation"
            )
        )

    else:
        insights.append(
            Insight(
                severity="NORMAL",
                metric="MEMORY",
                reason=f"Memory utilization for pod '{pod_id}' is within acceptable limits ({memory_usage:.2f})",
                recommendation="No action required"
            )
        )

    return insights