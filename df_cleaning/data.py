import pandas as pd

def get_data(artist_id):
    df = pd.read_csv(f"./bugs_database/merged/{artist_id}_merged.csv")
    return df
