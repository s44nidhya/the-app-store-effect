import json
import os
import pandas as pd




def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)




def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)



def save_df(df: pd.DataFrame, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)




def load_df(path: str) -> pd.DataFrame:
    return pd.read_csv(path)



def save_df(df: pd.DataFrame, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)




def load_df(path: str) -> pd.DataFrame:
    return pd.read_csv(path)