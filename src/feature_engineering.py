# src/feature_engineering.py

import pandas as pd

def engineer_features(df):
    """
    Engineers features from raw transaction data per wallet.
    """

    # Convert timestamp to datetime
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')

    # Convert amount to numeric USD value
    df['amount_usd'] = pd.to_numeric(df['actionData.amount'], errors='coerce') * pd.to_numeric(df['actionData.assetPriceUSD'], errors='coerce')

    # Group by wallet and engineer features
    grouped = df.groupby('userWallet').agg(
        total_deposits_usd = pd.NamedAgg(column='amount_usd', aggfunc=lambda x: x[df['action']=='deposit'].sum()),
        total_redeems_usd = pd.NamedAgg(column='amount_usd', aggfunc=lambda x: x[df['action']=='redeemunderlying'].sum()),
        txn_count = pd.NamedAgg(column='action', aggfunc='count'),
        unique_assets = pd.NamedAgg(column='actionData.assetSymbol', aggfunc=pd.Series.nunique),
        max_deposit_usd = pd.NamedAgg(column='amount_usd', aggfunc=lambda x: x[df['action']=='deposit'].max()),
        has_liquidation = pd.NamedAgg(column='action', aggfunc=lambda x: int('liquidationcall' in x.values)),
        avg_deposit_usd = pd.NamedAgg(column='amount_usd', aggfunc=lambda x: x[df['action']=='deposit'].mean()),
    ).reset_index()

    # Replace NaN with 0 for downstream consistency
    grouped.fillna(0, inplace=True)

    return grouped
