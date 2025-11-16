
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd
from agent.compliance_engine import ComplianceEngine
from utils.guardrails import validate_input, redact_pii, log_action, check_rate_limit, gdpr_note


gdpr_note()
st.title("AI Compliance Monitoring Agent")

if not check_rate_limit("compliance_queries"):
    st.stop()

uploaded_file = st.file_uploader("Upload compliance_transactions.csv", type="csv")
if uploaded_file:
    transactions = pd.read_csv(uploaded_file)
else:
    transactions = pd.read_csv("data/transaction_history.csv")  # Reuse as sample

# Redact PII
transactions = redact_pii(transactions)

if st.button("Check Compliance"):
    log_action("compliance_check", transactions.shape)
    try:
        if not pd.api.types.is_numeric_dtype(transactions['amount']):
            raise ValueError("Invalid input for amount: column must be numeric")
        engine = ComplianceEngine(transactions)
        results = engine.monitor_compliance()
        st.dataframe(results)
        violations = results[results['violation'] == True]
        if not violations.empty:
            st.error(f"Found {len(violations)} potential violations!")
    except ValueError as e:
        st.error(f"Guardrail Error: {e}")