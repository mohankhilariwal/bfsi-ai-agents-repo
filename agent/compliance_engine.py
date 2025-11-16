import pandas as pd
from langchain_openai import OpenAI

llm = OpenAI(temperature=0)

class ComplianceEngine:
    def __init__(self, transactions_df):
        self.df = transactions_df.copy()

    def monitor_compliance(self):
        self.df['violation'] = (self.df['amount'] > 10000) & (self.df['is_international'] == 1) & (self.df['frequency'] > 5)
        
        def explain(row):
            if row['violation']:
                prompt = f"Explain why this transaction might violate AML: Amount ${row['amount']}, International: {row['is_international']}, Frequency: {row['frequency']}."
                return llm.invoke(prompt)
            return "Compliant"
        
        self.df['explanation'] = self.df.apply(explain, axis=1)
        return self.df