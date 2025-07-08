# Customer Churn Prediction and Retention System

This project predicts which insurance customers are likely to churn and recommends targeted retention strategies to reduce cancellations.


## 🚀 Features

- 🔍 **Churn Prediction** using Logistic Regression
- 🧼 **Preprocessing** of real-world customer data (Telco dataset)
- 🧠 **Customer Segmentation** based on tenure, contract, and spending
- 🎯 **Retention Strategy Engine** to recommend personalized actions
- 📊 **Campaign Report** with churn risk, segment, and suggested actions


## 📁 Project Structure
customer-churn-retention/
├── data/                # Contains the Telco customer dataset
├── src/
│   ├── model.py         # Churn prediction model
│   ├── preprocess.py    # Data cleaning and encoding
│   ├── segment.py       # Customer segmentation logic
│   └── retention.py     # Retention strategy logic
├── reports/
│   └── campaign\_suggestions.csv   # Final strategy recommendations
├── campaign.py          # End-to-end pipeline
├── run\_model.py         # Quick test script for model
├── requirements.txt     # Python dependencies
└── README.md            # Project overview

## 🧠 How It Works

1. Load and preprocess the customer data (`preprocess.py`)
2. Train a Logistic Regression churn model (`model.py`)
3. Segment customers based on contract, tenure, etc. (`segment.py`)
4. Recommend retention strategies based on churn risk and segment (`retention.py`)
5. Generate a final campaign report (`campaign.py`)


## 🧪 How to Run
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the full campaign script
python campaign.py

## 📈 Sample Output

| Churn Risk | Segment      | Strategy                               |
| ---------- | ------------ | -------------------------------------- |
| 0.59       | New Customer | Onboarding Call + Welcome Discount     |
| 0.76       | Regular      | Send Promotional Email                 |
| 0.01       | Regular      | No Action Needed                       |
| 0.52       | High-Value   | Offer Loyalty Bonus or Premium Upgrade |

✅ Output saved in `reports/campaign_suggestions.csv`


## 📊 Dataset

* [Telco Customer Churn Dataset (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
