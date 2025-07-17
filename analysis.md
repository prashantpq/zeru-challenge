
---

## 📊 **2. `analysis.md` Template**

```markdown
# 📈 **Analysis Report: Wallet Credit Scoring**

## ✅ **1. Score Distribution**

Below is the **histogram of credit scores** across ranges:

| **Score Range** | **Number of Wallets** |
|---|---|
| 0-100 | xxx |
| 100-200 | xxx |
| 200-300 | xxx |
| ... | ... |
| 900-1000 | xxx |

> **Insert plot here:**  
> *(Attach matplotlib/seaborn bar plot showing counts per 100-score range bucket)*

---

## 🔍 **2. Behavioural Analysis**

### 🟥 **Low Score Wallets (0-200)**

- Characteristics:
  - Low or irregular deposits.
  - High borrow to repay ratio.
  - Frequent liquidations (if any).
  - Possible bot-like micro transactions.

---

### 🟩 **High Score Wallets (800-1000)**

- Characteristics:
  - Consistent deposits of significant value.
  - Responsible borrowing with timely repayments.
  - Zero or minimal liquidation history.
  - Stable, human-like transaction patterns.

---

## 📌 **3. Insights**

- **Most wallets cluster in [score range]** indicating general behaviour patterns.
- **Outliers detected** in low ranges, likely representing bots or exploit exploiters.

---

## 📂 **Next Steps**

- Integrate external risk data (oracle feeds, liquidation events) for improved scoring.
- Experiment with unsupervised clustering for risk segment detection.

---

## 👤 **Author**

Prashant Sharma  
[LinkedIn](#) | [GitHub](#)
