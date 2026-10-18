"""Validate source CSV and produce cleaned CSV and SQLite table."""
from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data/raw/champions_sample.csv'
OUT = ROOT / 'data/processed'
CLASSES = {'Cosmic', 'Tech', 'Mystic', 'Skill', 'Mutant', 'Science'}


def clean(df: pd.DataFrame) -> pd.DataFrame:
    required = {'name', 'class', 'immunities', 'offense', 'survivability', 'utility', 'source'}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f'Missing columns: {sorted(missing)}')
    result = df.copy()
    result['name'] = result['name'].astype('string').str.strip()
    result['class'] = result['class'].astype('string').str.strip()
    result['source'] = result['source'].astype('string').str.strip()
    result['immunities'] = result['immunities'].fillna('').astype(str).str.strip()
    if result['name'].isna().any() or result['name'].eq('').any():
        raise ValueError('Champion names cannot be blank')
    if result['name'].str.casefold().duplicated().any():
        raise ValueError('Duplicate champion names detected')
    if not result['class'].isin(CLASSES).all():
        raise ValueError('Unrecognized champion class')
    if result['source'].isna().any() or result['source'].eq('').any():
        raise ValueError('Every row requires a source')
    for column in ['offense', 'survivability', 'utility']:
        result[column] = pd.to_numeric(result[column], errors='coerce')
        if result[column].notna().any() and not result[column].dropna().between(0, 100).all():
            raise ValueError(f'{column} must be between 0 and 100')
    return result.sort_values('name').reset_index(drop=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    df = clean(pd.read_csv(RAW))
    df.to_csv(OUT / 'champions.csv', index=False)
    with sqlite3.connect(OUT / 'champions.db') as connection:
        connection.executescript((ROOT / 'sql/schema.sql').read_text())
        connection.execute('DELETE FROM champions')
        df.to_sql('champions', connection, if_exists='append', index=False)
    print(f'Validated {len(df)} records')


if __name__ == '__main__':
    main()
