
import sqlite3
import pandas as pd

connection = sqlite3.connect("data/processed/champions.db")

query = """
SELECT class, COUNT(*) AS champion_count
FROM collected_champions
GROUP BY class
ORDER BY champion_count DESC;
"""

result = pd.read_sql_query(query, connection)

print(result.to_string(index=False))

connection.close()
