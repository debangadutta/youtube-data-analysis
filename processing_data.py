import pandas as pd

df_raw = pd.read_json("./raw_data/json/IN_category_id.json")

df_flattened = pd.json_normalize(df_raw['items'])

df_flattened.to_parquet('./raw_data/parquet_files/IN_category.parquet')