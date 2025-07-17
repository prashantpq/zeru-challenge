# DeFi Credit Scoring Model

This project develops a robust machine learning pipeline to assign credit scores (0-1000) to wallets interacting with Aave V2 based on their historical transaction behavior.

## Problem

Assess DeFi user risk profiles from transaction-level data to enable credit risk assessment for decentralized lending protocols.

## Approach

1. **Feature Engineering:** Aggregated user transaction features such as total deposits, redeems, transaction count, unique assets, etc.
2. **Scoring Model:** Normalization-based scoring across engineered features to yield a final wallet score (0-1000).

## Project Structure

- `score_wallets.py`: Main entry script to generate scores.
- `src/feature_engineering.py`: Feature engineering logic.
- `src/scoring.py`: Scoring logic.
- `data/`: Sample input data.
- `notebooks/`: Exploratory Data Analysis.

## Requirements

- Python 3.8+
- pandas
- scikit-learn
- matplotlib

## Logic Behind Credit Scoring

### Goal

To assign **credit-like scores** to wallets based on their **transaction behaviors, liquidity, and protocol interactions**, thereby quantifying user reputation or financial activity within DeFi protocols.

---

### Feature Engineering Logic

Implemented in [`src/feature_engineering.py`](src/feature_engineering.py), the following features are engineered:

| Feature | Explanation |
|---|---|
| **total_deposits_usd** | Total USD value of deposits made by the wallet (**activity + liquidity**). |
| **total_redeems_usd** | Total USD value withdrawn or redeemed (fund outflows). |
| **txn_count** | Number of transactions (**frequency indicator**). |
| **unique_assets** | Number of distinct assets interacted with (**diversification measure**). |
| **max_deposit_usd** | Largest single deposit value (**risk capacity indicator**). |
| **has_liquidation** | Indicates whether the wallet faced liquidation (**risk history**). |
| **avg_deposit_usd** | Average deposit value, smoothing total deposits to typical transaction size. |

 **Why these features?**

These features combine **volume, frequency, diversification, and risk behavior**, aligning with both **traditional credit modeling** and emerging **DeFi risk assessment** best practices to derive a holistic user profile.

---

### Score Calculation Logic

Implemented in [`src/scoring.py`](src/scoring.py):

1. **Min-Max Scaling**

   - Each numeric feature is **scaled between 0 and 1000**, normalizing features across different units (e.g. USD vs count).

2. **Final Score Calculation**

   \[
   \text{Score} = \text{Mean of scaled features} \times 1000
   \]

3. **Rounding**

   - Scores are **rounded to the nearest integer** for clean interpretation and presentation.

---

 **This ensures:**

- All features contribute **equally** to the final score.  
- Scores range between **0 and 1000**, familiar to traditional credit risk scales and easy to integrate into downstream DeFi lending or incentive models.

---

### Score Interpretation

| Score Range | Meaning |
|---|---|
| **0 – 100** | Minimal activity; new or inactive wallet. |
| **100 – 500** | Low–moderate engagement. |
| **500 – 800** | Active user with significant protocol interactions. |
| **800 – 1000** | High-value wallet; potentially whales with diversified positions. |

---



