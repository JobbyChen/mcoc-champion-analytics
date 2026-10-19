
import pandas as pd

INPUT = "data/raw/champion_details_sample.csv"

df = pd.read_csv(INPUT)

valid_classes = {
    "Cosmic", "Tech", "Mystic",
    "Skill", "Mutant", "Science"
}

valid_tiers = {"S+", "S", "A", "B", "C", "D", "F"}

print(f"Total champions: {len(df)}")
print(f"Duplicate URLs: {df['source_url'].duplicated().sum()}")
print(f"Duplicate names: {df['name'].duplicated().sum()}")
print(f"Missing values: {df.isna().sum().sum()}")
print(f"Invalid classes: {(~df['class'].isin(valid_classes)).sum()}")
print(f"Invalid tiers: {(~df['tier'].isin(valid_tiers)).sum()}")

print("\nChampions by class:")
print(df["class"].value_counts())
