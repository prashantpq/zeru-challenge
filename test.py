import pandas as pd

df = pd.read_csv('wallet_scores.csv')
print(df['score'].describe())
print("Top 10 scores:\n", df.sort_values(by='score', ascending=False).head(10))
