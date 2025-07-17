# score_wallets.py

import json
import pandas as pd
from src.feature_engineering import engineer_features
from src.scoring import generate_scores

def main():
    """
    Runs the full pipeline:
    - Loads raw JSON data
    - Engineers features
    - Generates scaled wallet scores
    - Saves results to CSV
    """

    # Load data
    with open('data/user-wallet-transactions.json') as f:
        data = json.load(f)

    df = pd.json_normalize(data)

    # Feature Engineering
    features_df = engineer_features(df)

    # Generate Scores
    scores_df = generate_scores(features_df)

    # Save results
    scores_df.to_csv('wallet_scores.csv', index=False)
    print("✅ Wallet scores saved to wallet_scores.csv")

if __name__ == "__main__":
    main()
