import pandas as pd
import pytest
from scripts.clean_data import clean

BASE = {'name': 'Example', 'class': 'Tech', 'immunities': '', 'offense': 50, 'survivability': 50, 'utility': 50, 'source': 'test'}

def test_valid_record():
    assert len(clean(pd.DataFrame([BASE]))) == 1

def test_duplicate_names_rejected():
    with pytest.raises(ValueError, match='Duplicate'):
        clean(pd.DataFrame([BASE, {**BASE, 'name': ' example '}]))

def test_out_of_range_rejected():
    with pytest.raises(ValueError, match='between'):
        clean(pd.DataFrame([{**BASE, 'offense': 101}]))
