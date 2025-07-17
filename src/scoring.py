import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def generate_scores(df):
    """
    Generates a scaled score between 0-1000 for each wallet based on engineered features.
    """

    scaler = MinMaxScaler(feature_range=(0,1000))
    score_cols = ['total_deposits_usd', 'total_redeems_usd', 'txn_count', 'unique_assets', 'max_deposit_usd']

    df[score_cols] = scaler.fit_transform(df[score_cols])

    df['score'] = df[score_cols].mean(axis=1)
    df['score'] = (df['score'] / df['score'].max()) * 1000
    df['score'] = df['score'].round(0)

    return df[['userWallet','score']]
