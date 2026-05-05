from fastapi import FastAPI
from app.orchestrator.agent_orchestrator import run_analysis

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "AI Engine Running"}

@app.get("/analyze")
def analyze(pod_ids: str):

    if not pod_ids:
        return {"error": "No pod_ids provided"}

    pod_list = pod_ids.split(",")
    results = []

    for pod in pod_list:
        insights = run_analysis(pod.strip())
        results.append({
            "pod": pod.strip(),
            "insights": insights
        })

    return results