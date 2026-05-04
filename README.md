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
