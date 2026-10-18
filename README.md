# MCOC Champion Analytics

An original, data-first champion explorer inspired by the browsing experience at mcoc.app. Not affiliated with Kabam or mcoc.app.

## Current status
Starter scaffold with a working browser explorer, a small **illustrative** CSV dataset, a Python/Pandas cleaning script, SQLite schema, and a FastAPI endpoint. Sample numeric ratings are **not factual game statistics**. Do not publish them as measured or official rankings.

## Quick start: frontend
Open `frontend/index.html` in your browser. It uses a small embedded demonstration dataset so it works without a server.

## Python data pipeline
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/clean_data.py
uvicorn backend.main:app --reload
```
Visit `http://127.0.0.1:8000/docs`. The cleaner writes `data/processed/champions.csv` and `data/processed/champions.db`.

## Planned next steps
1. Find and inspect a reusable, appropriately licensed MCOC dataset.
2. Define data dictionary, sources, and provenance.
3. Expand cleaning tests, duplicate rules, and missing-data handling.
4. Connect React/TypeScript UI to the API and add comparisons.
5. Design transparent scoring, avoiding invented measurements.

## Data fields
`name`, `class`, `immunities`, `offense`, `survivability`, `utility`, `source`. Scores in sample are illustrative placeholders only.
