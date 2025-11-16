# BFSI AI Agents Repo

AI agents for Banking, Financial Services, and Insurance use cases. Includes basic guardrails (validation, rate limiting) and GDPR adaptations (PII redaction, no storage).

## Use Cases
1. **Fraud Detection**: Monitors transactions for anomalies.
2. **Credit Risk Assessment**: Evaluates loan risks.
3. **Customer Service Chatbot**: Handles queries via RAG.
4. **Compliance Monitoring**: Checks for regulatory violations.

## Setup
1. Clone repo.
2. `pip install -r requirements.txt`
3. Add OPENAI_API_KEY to `.env`.
4. Run: `streamlit run <app>.py`

## Guardrails & GDPR
- Validation & logging in `utils/guardrails.py`.
- PII hashed; in-memory processing only.
- For production: Enhance with full audits, consent forms.