 # preprocess.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(data_path):
    df = pd.read_csv(data_path)

    # Drop unnecessary columns
    df.drop(['customerID'], axis=1, inplace=True)

    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)

    # Encode categorical columns
    for col in df.select_dtypes(include='object').columns:
        if col != 'Churn':
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

    # Encode target
    df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

    return df

