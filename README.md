# DeFi Credit Scoring Model

This project develops a robust machine learning pipeline to assign credit scores (0-1000) to wallets interacting with Aave V2 based on their historical transaction behavior.

## 📊 Problem

Assess DeFi user risk profiles from transaction-level data to enable credit risk assessment for decentralized lending protocols.

## 💡 Approach

1. **Feature Engineering:** Aggregated user transaction features such as total deposits, redeems, transaction count, unique assets, etc.
2. **Scoring Model:** Normalization-based scoring across engineered features to yield a final wallet score (0-1000).

## ⚙️ Project Structure

- `score_wallets.py`: Main entry script to generate scores.
- `src/feature_engineering.py`: Feature engineering logic.
- `src/scoring.py`: Scoring logic.
- `data/`: Sample input data.
- `notebooks/`: Exploratory Data Analysis.

## 🛠️ Requirements

- Python 3.8+
- pandas
- scikit-learn
- matplotlib

Install dependencies:

