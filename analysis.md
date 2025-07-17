# Wallet Score Analysis

This analysis summarises the credit scores generated for wallets based on their Aave V2 transaction data.

## 📊 Score Distribution

Below is the distribution of wallet scores grouped into 100-point buckets.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wallet_scores.csv')

# Bin scores into ranges
bins = list(range(0, 1100, 100))
df['score_range'] = pd.cut(df['score'], bins)

# Plot
score_counts = df['score_range'].value_counts().sort_index()
score_counts.plot(kind='bar', figsize=(10,6))
plt.title('Wallet Credit Score Distribution')
plt.xlabel('Score Range')
plt.ylabel('Number of Wallets')
plt.show()
