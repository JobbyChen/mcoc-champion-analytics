"""Read-only API for validated champion data."""
from pathlib import Path
import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI(title='MCOC Champion Analytics API')
DB = Path(__file__).resolve().parents[1] / 'data/processed/champions.db'

@app.get('/health')
def health():
    return {'status': 'ok', 'database_ready': DB.exists()}

@app.get('/champions')
def champions(champion_class: str | None = None):
    if not DB.exists():
        raise HTTPException(status_code=503, detail='Run python scripts/clean_data.py first')
    with sqlite3.connect(DB) as conn:
        conn.row_factory = sqlite3.Row
        if champion_class:
            rows = conn.execute('SELECT * FROM champions WHERE class = ? ORDER BY name', (champion_class,)).fetchall()
        else:
            rows = conn.execute('SELECT * FROM champions ORDER BY name').fetchall()
    return [dict(row) for row in rows]
