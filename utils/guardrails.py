import hashlib
import logging
import streamlit as st
from datetime import datetime

logging.basicConfig(filename='bfsi_logs.txt', level=logging.INFO)

def validate_input(data, expected_types):
    """Basic input validation guardrail."""
    for key, val in data.items():
        if not isinstance(val, expected_types.get(key, object)):
            raise ValueError(f"Invalid input for {key}: {val}")
    return data

def redact_pii(df, pii_columns=['user_id', 'applicant_id']):
    """Basic GDPR: Anonymize PII by hashing."""
    for col in pii_columns:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest()[:10])  # Pseudonymize
    return df

def log_action(action, user_input):
    """Log actions without storing PII."""
    logging.info(f"{datetime.now()}: Action '{action}' with input size {len(str(user_input))}")

def check_rate_limit(session_key, max_queries=10):
    """Simulate rate limiting to prevent abuse."""
    if session_key not in st.session_state:
        st.session_state[session_key] = 0
    if st.session_state[session_key] >= max_queries:
        st.error("Rate limit exceeded. Please try later.")
        return False
    st.session_state[session_key] += 1
    return True

def gdpr_note():
    """Transparency note for GDPR/PIPEDA."""
    st.info("Data processed in-memory only. No persistent storage. PII anonymized. Consent implied by usage. For erasure/access, no data retained.")