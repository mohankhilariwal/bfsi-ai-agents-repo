from dotenv import load_dotenv
load_dotenv()



import streamlit as st
import pandas as pd
from agent.credit_engine import CreditEngine
from utils.guardrails import validate_input, redact_pii, log_action, check_rate_limit, gdpr_note


gdpr_note()
st.title("AI Credit Risk Assessment Agent")

if not check_rate_limit("credit_queries"):
    st.stop()

income = st.number_input("Annual Income ($)", min_value=0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850)
loan_amount = st.number_input("Loan Amount ($)", min_value=0)
applicant_data = pd.DataFrame({
    'income': [income],
    'credit_score': [credit_score],
    'loan_amount': [loan_amount]
})

if st.button("Assess Risk"):
    log_action("credit_assessment", applicant_data.to_dict())
    try:
        sample = applicant_data.iloc[0]
        validate_input(
            {
                'income': float(sample['income']),
                'credit_score': int(sample['credit_score']),
                'loan_amount': float(sample['loan_amount']),
            },
            {
                'income': float,
                'credit_score': int,
                'loan_amount': float,
            },
        )
        historical = pd.read_csv("data/credit_applications.csv")
        historical = redact_pii(historical, ['applicant_id'])
        applicant_data = redact_pii(applicant_data)  # No id, but for consistency
        engine = CreditEngine(historical)
        risk_score = engine.assess_risk(applicant_data)
        st.metric("Default Risk Score (0-1)", f"{risk_score[0]:.2f}")
        if risk_score > 0.3:
            st.warning("High risk - Review manually.")
        else:
            st.success("Low risk - Approve.")
    except ValueError as e:
        st.error(f"Guardrail Error: {e}")