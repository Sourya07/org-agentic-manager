# Pod Insight AI

Pod Insight AI is a production-oriented monorepo starter for an AI-powered real-time Kubernetes pod resource discovery, anomaly analysis, and dependency mapping platform.

This repository is being scaffolded iteratively so the structure stays intentional and easy for a team to evolve.

## What We Are Building

- A `Next.js` dashboard in `apps/web`
- An `Express.js + TypeScript` API in `apps/api`
- An optional background worker in `apps/worker`
- Shared workspace packages in `packages/*`
- Infrastructure assets in `infra/*`
- Project and architecture docs in `docs/*`

## Current Phase

The root monorepo scaffold is in place:

- `pnpm` workspace configuration
- `Turborepo` pipeline configuration
- top-level folder structure
- repository hygiene files

## Upcoming Phases

1. Scaffold the backend foundation in `apps/api`
2. Add feature-based domain modules for platform capabilities
3. Add shared package starters in `packages/*`
4. Add app starters for `apps/web` and `apps/worker`
5. Add docs, architecture guides, and API documentation
6. Add infra starters for local containers and Kubernetes manifests

## Planned Repository Shape

```text
pod-insight-ai/
  apps/
    web/
    api/
    worker/
  packages/
    ui/
    types/
    utils/
    config/
    sdk/
    prompts/
  infra/
    docker/
    k8s/
    scripts/
  docs/
  turbo.json
  package.json
  pnpm-workspace.yaml
  README.md
```

## Monorepo Goals

- Keep ownership clear across apps, packages, and backend modules
- Make parallel development easy for multiple engineers
- Standardize build, lint, test, and typecheck workflows
- Start with maintainable scaffolding instead of premature complexity

## Workspace Commands

These commands are wired at the root and will become active as app/package starters are added:

```bash
pnpm dev
pnpm build
pnpm lint
pnpm typecheck
pnpm test
```

## Status

This repository is intentionally incomplete at this stage. The next step is scaffolding the backend app structure in `apps/api` with feature-first modules, shared bootstrap patterns, and Swagger/OpenAPI support.

# AI Engine - Agentic Analysis Service

This service provides an agent-based analysis system for monitoring pod-level metrics and generating actionable insights.

## 🚀 Features

- FastAPI-based backend service
- Agent orchestration (CPU + Memory agents)
- Multi-pod analysis support
- Prometheus-ready metrics integration
- Modular and scalable architecture

---

## 🏗️ Project Structure
services/ai-engine/
├── app/
│ ├── agents/ # CPU & Memory agents
│ ├── orchestrator/ # Agent orchestration logic
│ ├── services/ # Metrics service (Prometheus)
│ ├── models/ # Response schemas
│ └── main.py # FastAPI entrypoint

---

## ⚙️ Setup

```bash
cd services/ai-engine
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt

▶️ Run Service
uvicorn app.main:app --reload

📡 API Endpoints
Health Check
GET /

Response:

{ "status": "AI Engine Running" }

Analyze Pods
GET /analyze?pod_ids=pod1,pod2

Response:

[
  {
    "pod": "pod1",
    "insights": [
      {
        "type": "cpu",
        "level": "HIGH",
        "message": "High CPU usage detected"
      }
    ]
  }
]

📊 Metrics Source
Uses Prometheus for fetching CPU and memory metrics
Configurable via .env

PROMETHEUS_URL=http://localhost:9090

🧠 Architecture
API receives pod IDs
Orchestrator triggers agents
Agents analyze metrics
Insights are aggregated and returned

🚧 Future Improvements
Real cluster integration
Authentication layer
Deployment on Kubernetes (EKS/GKE)
Advanced anomaly detection

👨‍💻 Author

AI Engine module for agentic system analysis

Developed as part of AI Engine module for agent-based system analysis
---

### 1. File update
- `README.md` open karo
- replace/add content

---

### 2. Commit
```bash
git add README.md
git commit -m "docs: update readme for ai engine service"
git push

