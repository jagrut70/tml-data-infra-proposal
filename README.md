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

## Architecture Overview

```mermaid
flowchart LR
    subgraph Sources[External Sources]
      W[Web / Crawler]:::src
      P[Partners / OSS Corpora]:::src
    end

    W -->|HTML/Media| K[(Kafka<br/>raw_html, media, metrics)]:::mq
    P --> K

    subgraph Proc[Processing]
      SS[Spark Structured Streaming<br/>(parse, normalize, extract)]:::compute
      RY[Ray Workers<br/>(embeddings/OCR/ASR)]:::compute
    end

    K --> SS
    SS -->|raw→landing| BR[(Delta: Bronze)]:::delta
    BR -->|curate + PII scrub| SL[(Delta: Silver)]:::delta
    SL -->|tiered dedup| DD[Dedup Pipeline<br/>(SHA256 → MinHash/SimHash → ANN)]:::service
    DD --> GD[(Delta: Gold<br/>Train Catalogs + Manifests)]:::delta

    subgraph Catalog[Discovery & Repro]
      DBT[dbt models + tests + docs]:::tool
      IDX[Search Index<br/>(BM25 + ANN)]:::tool
      MF[Dataset Manifests<br/>(semver + content address)]:::tool
    end

    GD --> DBT
    GD --> IDX
    GD --> MF

    subgraph Consumers[Researchers & Training]
      TR[Training Jobs]:::user
      EV[Evals / Slice Discovery]:::user
      VZ[Analytics / Viz]:::user
    end

    MF --> TR
    IDX --> EV
    GD --> TR
    GD --> EV
    DBT --> VZ

    classDef src fill:#e9f5ff,stroke:#5aa9e6,stroke-width:1.2;
    classDef mq fill:#fff2cc,stroke:#e6b800,stroke-width:1.2;
    classDef compute fill:#f5e9ff,stroke:#a05ae6,stroke-width:1.2;
    classDef delta fill:#e6ffe9,stroke:#34a853,stroke-width:1.2;
    classDef tool fill:#ffe9f2,stroke:#e65a9b,stroke-width:1.2;
    classDef service fill:#f0f0f0,stroke:#888,stroke-width:1.2;
    classDef user fill:#e8f7f0,stroke:#2aa198,stroke-width:1.2;
```

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

## Additional Documentation

For detailed system diagrams including:
- Deduplication Pipeline flow
- Orchestration & Reproducibility architecture  
- Dataset Build Sequence (Researcher POV)

See [docs/diagrams.md](docs/diagrams.md) for complete Mermaid diagrams.

---
Made with ❤️ as part of my application for **Software Engineer — Data Infrastructure**.

```bash
#!/bin/bash
# GitHub Logout Script
# Run this script to log out of your current GitHub account

echo "🔍 Checking current Git configuration..."
echo "Current user name: $(git config --global user.name)"
echo "Current user email: $(git config --global user.email)"

echo ""
echo "🚪 Logging out of GitHub..."

# Clear Git user configuration
echo "Clearing Git user configuration..."
git config --global --unset user.name
git config --global --unset user.email

# Clear GitHub credentials from macOS keychain
echo "Clearing GitHub credentials from keychain..."
echo "host=github.com" | git credential-osxkeychain erase
echo "protocol=https" | git credential-osxkeychain erase

# Alternative method to clear keychain
echo "Using security command to clear GitHub credentials..."
security delete-internet-password -s github.com 2>/dev/null || echo "No GitHub credentials found in keychain"

# If GitHub CLI is installed, logout from there too
if command -v gh &> /dev/null; then
    echo "Logging out from GitHub CLI..."
    gh auth logout
fi

echo ""
echo "✅ GitHub logout complete!"
echo ""
echo "🔍 Verifying logout..."
echo "User name: $(git config --global user.name)"
echo "User email: $(git config --global user.email)"

echo ""
echo "📝 Next time you try to access GitHub, you'll be prompted to authenticate again."
```
