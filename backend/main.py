from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import sqlite3

from fastapi import FastAPI

app = FastAPI(title="MCOC Champion Analytics API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
DB_PATH = Path(__file__).resolve().parents[1] / "data/processed/champions.db"


@app.get("/")
def home():
    return {"message": "MCOC Champion Analytics API is running"}



@app.get("/champions")
def get_champions(champion_class: str | None = None, tier: str | None = None):
    query = """
        SELECT name, class, tier, source_url
        FROM collected_champions
        WHERE 1=1
    """
    parameters = []

    if champion_class:
        query += " AND class = ?"
        parameters.append(champion_class)

    if tier:
        query += " AND tier = ?"
        parameters.append(tier)

    query += " ORDER BY name"

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(query, parameters).fetchall()

    return [dict(row) for row in rows]

@app.get("/analytics/classes")
def get_class_analytics():
    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row

        rows = connection.execute("""
            SELECT class, COUNT(*) AS champion_count
            FROM collected_champions
            GROUP BY class
            ORDER BY champion_count DESC
        """).fetchall()

    return [dict(row) for row in rows]
