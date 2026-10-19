
import sqlite3
from pathlib import Path

import pandas as pd

CSV_PATH = Path("data/raw/champion_details_sample.csv")
DB_PATH = Path("data/processed/champions.db")

# Read the validated champion data
df = pd.read_csv(CSV_PATH)

# Connect to the SQLite database
with sqlite3.connect(DB_PATH) as connection:

    # Create or replace a table for our collected data
    df.to_sql(
        "collected_champions",
        connection,
        if_exists="replace",
        index=False
    )

    # Verify the database contains our records
    result = pd.read_sql_query(
        "SELECT name, class, tier FROM collected_champions",
        connection
    )

print(result.to_string(index=False))
print(f"\nLoaded {len(result)} champions into SQLite.")

