# campaign.py

import pandas as pd
from src.preprocess import load_and_preprocess
from src.model import train_churn_model
from src.segment import segment_customer
from src.retention import recommend_strategy

from sklearn.linear_model import LogisticRegression

def run_campaign(data_path):
    # Load and preprocess data
    df = load_and_preprocess(data_path)

    # Train model
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    churn_probabilities = model.predict_proba(X)[:, 1]  # Get churn risk scores

    # Add churn risk to dataframe
    df['Churn_Risk'] = churn_probabilities

    # Decode Contract back to original form for better segmenting
    contract_map = {0: 'Month-to-month', 1: 'One year', 2: 'Two year'}
    df['Contract'] = df['Contract'].map(contract_map)

    # Apply segmentation and retention strategies
    df['Segment'] = df.apply(segment_customer, axis=1)
    df['Strategy'] = df.apply(lambda row: recommend_strategy(row['Churn_Risk'], row['Segment']), axis=1)

    # Select key columns for report
    report = df[['Churn_Risk', 'Segment', 'Strategy']].head(10)  # Preview top 10

    print("\n📊 Churn Prevention Campaign Suggestions (Top 10 Customers):\n")
    print(report)

    # Optionally save to CSV
    report.to_csv('reports/campaign_suggestions.csv', index=False)
    print("\n✅ Report saved to reports/campaign_suggestions.csv")

# Run the campaign
if __name__ == "__main__":
    run_campaign("data/customer_data.csv")
