import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class FraudEngine:
    def __init__(self, transactions_df):
        self.df = transactions_df.copy()
        scaler = StandardScaler()
        self.df[['amount', 'time_of_day']] = scaler.fit_transform(self.df[['amount', 'time_of_day']])

    def detect_fraud(self):
        model = IsolationForest(contamination=0.05, random_state=42)
        features = self.df[['amount', 'time_of_day', 'is_international']]
        scores = model.fit_predict(features)
        self.df['fraud_score'] = [-s if s < 0 else 0 for s in model.decision_function(features)]  # Higher = more anomalous
        # Guardrail: Flag only if confidence > 0.1
        self.df['flagged'] = self.df['fraud_score'] > 0.1
        return self.df