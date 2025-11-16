import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class CreditEngine:
    def __init__(self, historical_df):
        self.historical = historical_df.copy()
        scaler = StandardScaler()
        self.historical[['income', 'credit_score', 'loan_amount']] = scaler.fit_transform(
            self.historical[['income', 'credit_score', 'loan_amount']]
        )
        X = self.historical[['income', 'credit_score', 'loan_amount']]
        y = self.historical['defaulted']
        self.model = LogisticRegression().fit(X, y)
        self.scaler = scaler

    def assess_risk(self, applicant_df):
        scaled = self.scaler.transform(applicant_df)
        risk_prob = self.model.predict_proba(scaled)[:, 1]  # Probability of default (class 1)
        return risk_prob