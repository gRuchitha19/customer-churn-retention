# model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

def train_churn_model(data_path):
    # Load data
    df = pd.read_csv(data_path)

    # Drop customerID (not useful)
    df = df.drop(['customerID'], axis=1)

    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()  # Drop rows with missing TotalCharges

    # Encode categorical variables
    for column in df.select_dtypes(include=['object']).columns:
        if column != 'Churn':
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])

    # Encode target
    df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

    # Split features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print("Classification Report:\n")
    print(classification_report(y_test, y_pred))

    return model
