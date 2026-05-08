# Architecture

This repository is a workflow starter for public-data competitor reporting.

It is organized around small runnable examples, provider-neutral data access, simple metrics, and report outputs.

## Layers

```text
examples/
  Runnable workflow recipes.

src/providers/
  Data provider adapters.

src/metrics/
  Metric calculation and text extraction.

src/reports/
  Markdown and HTML report rendering.

data/
  Mock fixtures and sample account lists.

reports/
  Generated sample outputs.

docs/
  Usage, production, and trust documentation.

benchmarks/
  Benchmark rules, raw data, and scripts.
```

## Design Principles

### Mock Data First

The default workflow runs without an API key.

This lets developers inspect the report shape, modify recipes, and understand the workflow before choosing a production provider.

### Provider-Neutral Reporting

Provider adapters normalize external data into the shared data model.

Metrics and report rendering should not depend on provider-specific response shapes.

### Report-First Output

The project prioritizes useful artifacts:

- Markdown reports
- HTML reports
- CSV-friendly metrics

Dashboards and integrations can be built later on top of these outputs.

### Production Docs Separate From README

README stays focused on trust, quick start, examples, and navigation.

Production decisions live in `docs/production/`, where provider comparison, cost control, deployment, and observability can be discussed with more context.

### Commercial Links Stay Contextual

Affiliate or commercial links should only appear where directly relevant to a production decision.

They should have nearby disclosure and should not replace the open-source path.

## Main Workflow

```text
account list
  -> provider adapter
  -> normalized profile/media records
  -> metrics and extraction
  -> Markdown / HTML / CSV-friendly outputs
```

## Extension Points

Common extension points:

- add a provider adapter in `src/providers/`
- add metrics in `src/metrics/`
- customize report rendering in `src/reports/`
- add examples in `examples/`
- add production notes in `docs/production/`

Keep extensions focused on public-data reporting workflows.
