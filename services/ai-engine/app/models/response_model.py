from pydantic import BaseModel
from typing import List


class Insight(BaseModel):
    severity: str
    metric: str
    reason: str
    recommendation: str


class AnalysisResponse(BaseModel):
    pod_id: str
    insights: List[Insight]