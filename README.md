# Thinking Machines Lab — Data Infrastructure Proposal (Repo Skeleton)

This repo is a **work-sample skeleton** showing how I'd approach building a petabyte‑scale training data platform:
- Distributed ingest (crawler → Kafka)
- Spark Structured Streaming to Delta (Bronze/Silver/Gold)
- Tiered dedup (SHA256 → MinHash/SimHash → ANN embeddings)
- dbt models + docs for reproducibility
- Airflow orchestration
- Terraform IaC
- Ray workers for embedding/OCR heavy tasks
- Observability (audit logs, SLOs, runbooks)

> This is intentionally lightweight and safe to share publicly — no secrets, only scaffolding + runnable stubs.

## Quick Start (local dev / demo)
```bash
# 1) Create a Python env (3.10+ recommended)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2) Run the simple dedup demo
python notebooks/dedup_demo.py

# 3) (Optional) Run the Spark job locally against example Kafka config (mock)
python spark_jobs/stream_to_delta.py --config configs/local.example.json

# 4) Render dbt docs (models are illustrative only)
#   Configure your profiles.yml manually as needed
dbt deps && dbt seed && dbt run && dbt test && dbt docs generate
```

## Layout
```
.
├── airflow/dags/                  # Airflow DAGs (idempotent, backfillable)
├── crawler/                       # Scrapy-based polite crawler skeleton
├── dbt/                           # dbt project (Delta/Parquet models + tests)
├── infra/terraform/               # Terraform IaC modules + env compositions
├── notebooks/                     # Small, self-contained demos (dedup)
├── ray_workers/                   # Ray tasks for embeddings/OCR
├── scripts/                       # Utility scripts (manifests, hashing, etc.)
├── spark_jobs/                    # Spark Structured Streaming + batch jobs
├── docker/                        # Optional local containers for demo
├── configs/                       # Example JSON/TOML configs (no secrets)
├── requirements.txt
├── LICENSE
└── README.md
```

---
Made with ❤️ as part of my application for **Software Engineer — Data Infrastructure**.
