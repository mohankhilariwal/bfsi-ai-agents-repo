
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd
from agent.fraud_engine import FraudEngine
from utils.guardrails import validate_input, redact_pii, log_action, check_rate_limit, gdpr_note


gdpr_note()
st.title("AI Fraud Detection Agent")

if not check_rate_limit("fraud_queries"):
    st.stop()

uploaded_file = st.file_uploader("Upload transaction_history.csv", type="csv")
if uploaded_file:
    transactions = pd.read_csv(uploaded_file, engine="python")
else:
    transactions = pd.read_csv("data/transaction_history.csv")

# Redact PII
transactions = redact_pii(transactions)

if st.button("Detect Fraud"):
    log_action("fraud_detection", transactions.shape)
    try:
        sample_amount = transactions['amount'].iloc[0]
        validate_input({'amount': sample_amount}, {'amount': (int, float)})
        #validate_input({'amount': transactions['amount'].dtype}, {'amount': float})
        engine = FraudEngine(transactions)
        results = engine.detect_fraud()
        st.dataframe(results)
        flagged = results[results['fraud_score'] > 0.5]
        if not flagged.empty:
            st.warning(f"Flagged {len(flagged)} suspicious transactions!")
    except ValueError as e:
        st.error(f"Guardrail Error: {e}")