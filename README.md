# DeFi Wallet Credit Scoring

## 📌 **Problem Statement**

This project builds a **machine learning-based credit scoring system** to assign scores between **0 and 1000** for wallets interacting with the Aave V2 protocol. Higher scores indicate reliable and responsible behaviour, while lower scores indicate risky, exploitative, or bot-like activity.

---

## 🛠 **Methodology**

1. **Input:** Raw transaction-level data from Aave V2 containing actions:
   - `deposit`, `borrow`, `repay`, `redeemunderlying`, `liquidationcall`.

2. **Feature Engineering:**
   - **Number of deposits**
   - **Total deposited amount**
   - **Average deposit size**
   - **Number of borrows**
   - **Total borrowed amount**
   - **Repayment ratio (total repaid / total borrowed)**
   - **Number of liquidations**

3. **Scoring Logic:**
   - Each wallet's engineered features are aggregated.
   - Scores are normalised between **0 and 1000** using min-max scaling.
   - Weighted scoring is applied based on feature importance to determine final credit scores.

---

## ⚙️ **Architecture & Processing Flow**

```mermaid
graph TD;
    A[Raw JSON file] --> B[Load DataFrame];
    B --> C[Feature Engineering];
    C --> D[Score Calculation];
    D --> E[Output CSV with wallet credit scores];
