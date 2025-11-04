import pandas as pd

def clean_data(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
