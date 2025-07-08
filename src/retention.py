 # retention.py

def recommend_strategy(churn_risk, segment):
    """
    Recommend a retention strategy based on churn probability and segment
    """
    if churn_risk < 0.3:
        return "No Action Needed"
    
    if segment == "High-Value":
        return "Offer Loyalty Bonus or Premium Upgrade"
    elif segment == "New Customer":
        return "Onboarding Call + Welcome Discount"
    elif segment == "Loyal":
        return "Exclusive Renewal Offer"
    elif segment == "Low-Value":
        return "Send Feedback Survey"
    else:
        return "Send Promotional Email"

