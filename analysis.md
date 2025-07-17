# Wallet Scoring Analysis

## Overview

This analysis summarizes the scoring of user wallets based on their DeFi transaction data. The pipeline included:

1. **Data Loading** – Reading transaction records from the JSON dataset.
2. **Feature Engineering** – Generating meaningful aggregated features per wallet.
3. **Scoring** – Scaling features and calculating a composite wallet score.

---

## Feature Engineering

The following features were engineered for each wallet:

| Feature Name          | Description |
|------------------------|-------------|
| `total_deposits_usd`  | Total deposit amount in USD. |
| `total_redeems_usd`   | Total redeemed amount in USD. |
| `txn_count`           | Total transaction count. |
| `unique_assets`       | Number of unique assets interacted with. |
| `max_deposit_usd`     | Maximum deposit amount in USD. |
| `has_liquidation`     | Whether the wallet had any liquidation events (1 or 0). |
| `avg_deposit_usd`     | Average deposit amount in USD. |

---

## Scoring Methodology

- **Scaler Used**: `MinMaxScaler` with feature range (0, 1000).
- **Score Calculation**: Mean of scaled features multiplied by 1000, rounded to integer.

---

## Final Score Summary

| Statistic | Value |
|-----------|-------|
| **Count** | 3497 wallets |
| **Mean** | ~60.31 |
| **Std** | ~84.61 |
| **Min** | 0 |
| **25%** | 0 |
| **50% (Median)** | 40 |
| **75%** | 81 |
| **Max** | 1000 |

- The top scoring wallet achieved **1000**, indicating dominant DeFi activity relative to peers.

---

## Output

Final wallet scores are saved to: wallet_scores.csv 



