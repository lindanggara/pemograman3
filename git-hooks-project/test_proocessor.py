import pandas as pd
from data_processor import process_data

def test_process_data_with_na():
    df = pd.DataFrame({'col1': [1, 2, None]})
    cleaned_df = process_data(df)
    assert cleaned_df.isnull().sum().sum() == 0
