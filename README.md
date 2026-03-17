# Detecting Structured Data Quality Violations in Retail Datasets

**Bachelor Thesis** — Uppsala University, Department of Information Technology (15 hp)

- **Author:** Muhammad Saad
- **Supervisor:** Paulina Kristiansson (Wolt)
- **Period:** HT26 (September – November 2026)

## Research Question

> How effectively can statistical and unsupervised machine learning methods detect structured data quality violations in retail product datasets?

## Overview

This project compares three approaches for detecting data quality violations in retail product datasets:

1. **Rule-based baseline** — deterministic validation against a known schema
2. **Statistical methods** — z-score and distribution-based anomaly detection
3. **Unsupervised ML** — Isolation Forest and Local Outlier Factor (LOF)

These methods are evaluated against four violation categories:

- **Completeness** — missing required values
- **Domain** — values outside allowed categories
- **Range** — numerical values outside valid bounds
- **Cross-field** — logical inconsistencies between related fields

## Project Structure

```
thesis-dq-detection/
├── config/              # Experiment configs, schema definitions, thresholds
├── data/
│   ├── raw/             # Clean baseline dataset
│   └── injected/        # Datasets with injected violations
├── notebooks/           # Exploratory analysis and visualizations
├── src/
│   ├── baseline/        # Rule-based validation
│   ├── statistical/     # Z-score / distribution-based detection
│   ├── unsupervised/    # Isolation Forest, LOF
│   └── evaluation/      # Metrics computation, result aggregation
├── tests/               # Unit tests
├── latex/               # Thesis LaTeX source
├── .gitignore
├── requirements.txt
└── README.md
```

## Tech Stack

- Python 3.11+
- Pandas / NumPy
- Scikit-learn
- SciPy
- Matplotlib / Seaborn

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
