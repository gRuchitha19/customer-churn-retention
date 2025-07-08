 # segment.py

def segment_customer(row):
    """
    Rule-based segmentation based on tenure, monthly charges, and contract type
    """
    if row['tenure'] >= 12 and row['MonthlyCharges'] > 80:
        return 'High-Value'
    elif row['tenure'] < 3:
        return 'New Customer'
    elif row['Contract'] == 2:  # 2 = Two year contract (already encoded)
        return 'Loyal'
    elif row['MonthlyCharges'] < 40:
        return 'Low-Value'
    else:
        return 'Regular'

