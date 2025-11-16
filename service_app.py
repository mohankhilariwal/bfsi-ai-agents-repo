from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from agent.service_engine import ServiceEngine
from utils.guardrails import log_action, check_rate_limit, gdpr_note, validate_input

gdpr_note()
st.title("AI Customer Service Chatbot Agent")

if not check_rate_limit("service_queries", max_queries=20):
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about account, loans, etc."):
    try:
        validate_input({'prompt': prompt}, {'prompt': str})
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            engine = ServiceEngine()
            response = engine.handle_query(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            log_action("service_query", prompt)
    except ValueError as e:
        st.error(f"Guardrail Error: {e}")