# BFSI AI Agents – Fraud, Credit, Service & Compliance

Intelligent AI and agentic workflows for **Banking, Financial Services & Insurance (BFSI)** – focusing on **fraud detection, credit risk, customer service, and compliance monitoring** with practical guardrails.

---

## Executive Summary

This repository showcases a set of **end-to-end AI/GenAI/Agentic AI prototypes** for BFSI organizations. It demonstrates how data science, classical ML, and LLM/RAG components can be combined into **interactive agents** that help:

- Detect suspicious payments and transactional fraud  
- Assess credit risk from structured customer data  
- Provide AI-assisted customer service on BFSI products and policies  
- Monitor activities for basic policy/regulatory breaches  

The repo is designed for:

- **Business leaders:** Heads of Fraud, Risk, Operations, Compliance, Cards, Digital & CX  
- **Data/AI teams:** Data scientists, MLOps, ML engineers, solution architects  
- **Innovation & product teams:** POC/experimentation squads and CoEs  
- **Recruiters & hiring managers:** Quick view of hands-on BFSI AI capabilities  

### Headline Outcomes (Illustrative Only)

If adapted to a real financial institution with proper data, governance, and integration, such agents can support:

- **10–30% reduction** in fraud-related manual review volumes (illustrative)  
- **15–25% faster loan decisioning** through triage and better risk segmentation (illustrative)  
- **20–40% lower contact-center load** on repetitive queries via AI-assisted answers (illustrative)  
- **30–50% faster first-line compliance checks** for basic policy breaches (illustrative)  

> All figures are **indicative only**, based on typical industry patterns from similar initiatives. Actual results depend entirely on data quality, process maturity, and organizational readiness.

---

## Use Cases / Agents Overview

The repo contains four primary Streamlit apps (agents), each mapped to a core BFSI problem:

1. **Fraud Detection Agent (`fraud_app.py`)**  
   - Monitors transactional data for anomalous behavior and potential fraud.  
   - Helps risk and operations teams prioritize which transactions or accounts to review.  

2. **Credit Risk Assessment Agent (`credit_app.py`)**  
   - Scores loan/credit applications using risk features (income, liabilities, behavior, etc.).  
   - Supports underwriters with a transparent risk view and indicative segmentation.  

3. **Customer Service / BFSI Support Agent (`service_app.py`)**  
   - RAG-style agent that answers customer or internal-ops questions based on a knowledge base.  
   - Focused on banking products, cards, fees, limits, dispute flows, etc. (demo content).  

4. **Compliance Monitoring Agent (`compliance_app.py`)**  
   - Scans activity/records against configurable policy rules.  
   - Highlights basic red flags for KYC/AML, sanctions, and conduct-policy breaches (demo only).  

### Typical Impact Metrics (Illustrative)

For each agent, examples of the type of impact stakeholders may target:

- **Fraud Agent:**  
  - Lower false positives & fewer “good customer” blocks  
  - Faster alert triage and case creation  
  - Better transparency on risk scores and reasons  

- **Credit Agent:**  
  - Shorter “time-to-yes/no” on applications  
  - More consistent decisioning across segments  
  - Early visibility into high-risk portfolios  

- **Service Agent:**  
  - Reduced call/chat volumes for FAQs  
  - Higher first-contact resolution (FCR) for standard queries  
  - 24/7 support on basic product and policy questions  

- **Compliance Agent:**  
  - Fewer missed basic policy breaches in first-line checks  
  - Better documentation trail for audits  
  - Faster review cycles for simple cases  

All of the above are **conceptual targets**, not guarantees.

---

## Common Architecture & Tech Stack

All four agents share a **common architectural pattern**:

1. **UI Layer – Streamlit Apps**  
   - Each agent is an individual Streamlit app (`fraud_app.py`, `credit_app.py`, `service_app.py`, `compliance_app.py`).  
   - Users interact via simple web forms, file upload widgets, and results dashboards.

2. **Data Layer – Sample CSV Inputs (under `data/`)**  
   - Demo CSVs representing:  
     - Transaction histories  
     - Credit/loan applications  
     - Customer interaction logs or support tickets  
     - Simple compliance or customer records  
   - In a real setup, these would be replaced by data warehouse tables, APIs, or streaming sources.

3. **Analytics & ML Layer**  
   - Illustrative use of classical ML and analytics concepts such as:  
     - **Anomaly detection** for fraud (e.g., unsupervised/supervised scoring logic)  
     - **Risk scoring** and segmentation logic for credit applications  
     - Basic **text search / retrieval** for RAG-like service responses  
     - Simple **rule/threshold engines** for compliance flags  

4. **Agent & Orchestration Layer (`agent/`)**  
   - Encapsulates agent-specific logic: tools, utility functions, and orchestration patterns.  
   - Provides reusable functions that each Streamlit app calls (e.g., scoring helpers, retrieval functions, rule evaluators).

5. **Guardrails & Utilities (`utils/`)**  
   - Basic building blocks for:
     - Input schema validation  
     - PII handling and hashing/pseudonymization  
     - Rate limiting and simple usage controls  
     - Centralized logging (e.g., `bfsi_logs.txt`)  

6. **Configuration & Secrets**  
   - `.env`-based configuration (e.g., `OPENAI_API_KEY` or other LLM/embedding keys).  
   - In real deployments these should be managed via secure secrets management, not plain `.env` files.

### Technology Stack (High-Level)

- **Language:** Python 3.x  
- **UI:** Streamlit  
- **Data & ML:** Typical Python data stack (e.g., pandas, numpy, scikit-learn or analogous), plus custom scoring logic  
- **LLM / RAG (for service agent):**  
  - LLM access via API (e.g., OpenAI or similar)  
  - Embedding-based retrieval or simple vector search for knowledge base lookups  
- **Configuration & Utilities:**  
  - `.env` / environment variables for secrets  
  - Utility modules under `utils/` for guardrails and logging  

For exact dependencies, see `requirements.txt` in the repo.

### Data Flow (Simplified)

1. **User uploads or selects sample data** from `data/` via Streamlit.  
2. **Input validation & PII handling** performed by utility functions.  
3. **Core analytics/ML/LLM logic** runs via the appropriate agent module.  
4. **Results scored and enriched** with flags, explanations, and segments.  
5. **Output visualized** via Streamlit tables, charts, and summaries.  
6. **Logs and metrics** (non-PII) can be persisted for analysis during development.

---

## Detailed Use Cases

Each of the following sections describes one agent in depth.

---

### 1. Fraud Detection Agent

#### Overview

The **Fraud Detection Agent** ingests payment or account transaction data and surfaces **suspicious patterns** that may indicate fraud. It is aimed at:

- Cards & payments fraud teams  
- Transaction banking operations  
- Risk analysts & fraud strategy teams  

#### Problem Statement

- Rising **digital and card payments volumes** make it impossible to manually review all alerts.  
- **High false-positive rates** cause customer friction (unnecessary declines/blocks).  
- Fraud teams are often overwhelmed by **unprioritized alerts** with little context.  
- Fragmented systems make it hard to **trace end-to-end customer behavior**.

#### Solution Architecture

- **Inputs (demo):**  
  - CSV transactions (e.g., account id, timestamp, merchant, amount, channel, location, device info, etc.).

- **Core Logic (illustrative):**  
  - Feature engineering for transaction velocity, amount deviations, geo-device inconsistency, merchant risk, etc.  
  - Anomaly detection and/or supervised fraud propensity scoring (e.g., risk score 0–1).  
  - Rule overlay (e.g., large amount + high-risk merchant + unusual location).

- **Guardrails:**  
  - Pseudonymization of account identifiers (hashing).  
  - Validation of required columns and data types.  
  - Input size constraints and simple rate limiting to avoid abuse.

- **Outputs:**  
  - Per-transaction **fraud risk score** and risk bands (e.g., low/medium/high).  
  - Ranked list of top suspicious transactions.  
  - Simple explanations/rationale (e.g., “unusual geolocation and high risk merchant”).

#### Key Features

- Batch scoring of uploaded transactional files via Streamlit UI.  
- Configurable thresholds for **risk bands**.  
- Summary statistics: distribution of risk scores, number of high-risk records.  
- Pseudonymization of customer IDs to avoid direct exposure of PII.  
- Logging of **non-PII metrics** and errors into logs for debugging.  
- Extensible feature-engineering and rule definitions in code.

#### Example Workflow

1. Launch the app and upload a CSV of transactions.  
2. Validate the schema (columns) and format in the UI.  
3. Click “Score Transactions” to run anomaly/propensity logic.  
4. Review the ranked list of high-risk transactions and risk summaries.  
5. Export results (e.g., CSV download) for downstream fraud case management.

#### Implementation Roadmap (Real BFSI)

- **Phase 1 – PoC**  
  - Use 1–3 months of historical transactional data.  
  - Benchmark against existing fraud rules and alert volumes.  
  - Validate model behavior with fraud analysts.

- **Phase 2 – Integration & Hardening**  
  - Connect to transaction streams/data warehouse.  
  - Add model monitoring (drift, alert volumes, false positives).  
  - Integrate with case management system (work queues, investigation notes).

- **Phase 3 – Scale & Continuous Improvement**  
  - Champion–challenger models; refine thresholds and features.  
  - Expand to new products/channels (e.g., wire, ACH, P2P).  
  - Embed within overall Enterprise Fraud Management (EFM) architecture.

#### Indicative ROI & KPIs

- 10–20% reduction in manual review workload (illustrative).  
- 5–15% improvement in detection of truly fraudulent transactions (illustrative).  
- Lower customer complaints related to false declines.  
- Faster time to detect and block fraud rings.

---

### 2. Credit Risk Assessment Agent

#### Overview

The **Credit Risk Assessment Agent** processes loan or credit-card application data and provides an **indicative risk score** with optional segmentation. It is not a replacement for full underwriting, but a **triage and decision-support tool**.

#### Problem Statement

- Underwriters face **high volumes** of applications with varying complexity.  
- Decisioning is often **manual and inconsistent** across analysts or branches.  
- Limited visibility into **portfolio-level risk distribution** until much later.  
- Regulatory focus on **fair lending, explainability, and bias** is increasing.

#### Solution Architecture

- **Inputs (demo):**  
  - CSV of credit applications (e.g., customer demographics, income, obligations, bureau scores, product type, requested limit).

- **Core Logic (illustrative):**  
  - Basic feature engineering (DTI ratios, utilization, length of relationship, delinquencies, etc.).  
  - Risk scoring function (e.g., low/medium/high risk tiers) or simple ML model.  
  - Rules to flag applications for manual review (e.g., borderline cases, missing data).

- **Guardrails:**  
  - Pseudonymization or removal of direct identifiers.  
  - Awareness flags for potentially sensitive features (e.g., protected attributes) to avoid direct use.  
  - Basic documentation on what features are used vs. not used.

- **Outputs:**  
  - Application-level risk scores and risk tiers.  
  - Summary dashboards (counts by risk segment, product, region).  
  - Explanatory notes of what influenced the risk tier (at a simple level).

#### Key Features

- Bulk scoring via CSV upload with schema validation.  
- Simple segmentation for triaging (e.g., auto-approve, manual review, auto-decline candidates).  
- Aggregated dashboards to understand **portfolio shape** in the sample.  
- Hooks to plug in more advanced models (e.g., logistic regression, gradient boosting, or institution’s internal models).  
- Basic logging for audit/debug (inputs summary, model version, scoring timestamps).

#### Example Workflow

1. Upload a sample credit applications CSV via the Streamlit interface.  
2. Validate required fields and run the scoring step.  
3. View risk tiers per application in a table with filters.  
4. Inspect portfolio distribution (e.g., % high risk by region or product).  
5. Export scores for downstream underwriting or decision engines.

#### Implementation Roadmap (Real BFSI)

- **Phase 1 – Prototype**  
  - Use de-identified historical data from one product (e.g., credit cards).  
  - Compare model output with actual defaults and existing scorecards.

- **Phase 2 – Integration & Governance**  
  - Embed into pre-decisioning workflows.  
  - Add explainability tools, back-testing, and bias assessments.  
  - Align with model risk management (MRM) frameworks and regulatory guidance.

- **Phase 3 – Enterprise Rollout**  
  - Expand to multiple products (mortgages, personal loans, SME credit).  
  - Integrate with collections and pricing strategies.  
  - Continuous monitoring & retraining via MLOps.

#### Indicative ROI & KPIs

- Shorter decisioning times (e.g., 15–30% faster for straightforward cases – illustrative).  
- Better risk alignment (fewer mispriced/high-risk approvals).  
- Improved consistency in underwriting decisions.  
- Stronger documentation for audits & regulators.

---

### 3. Customer Service / BFSI Support Agent (RAG-Based)

#### Overview

The **Customer Service Agent** is a **RAG-style knowledge assistant** that responds to banking/insurance queries using a curated knowledge base (e.g., FAQs, policy PDFs, product descriptions). It aims to support:

- Contact center agents (internal copilot)  
- Self-service portals and chat interfaces  
- Digital banking “help” sections  

#### Problem Statement

- Contact centers face **high volumes of repetitive queries**: card limits, fees, chargebacks, KYC requirements, etc.  
- Complex policies and product terms are **hard to navigate** in real time.  
- Inconsistent or outdated answers cause **customer dissatisfaction and risk**.  

#### Solution Architecture

- **Inputs (demo):**  
  - Text or CSV knowledge base for BFSI FAQs and policies.  
  - User query via Streamlit text box.

- **Core Logic (illustrative):**  
  - Embedding-based retrieval of relevant knowledge base chunks.  
  - Prompt composition with retrieved context.  
  - LLM call to generate a concise, policy-aligned response.

- **Guardrails:**  
  - Restrict responses to only what’s in the provided knowledge base (avoid hallucinations as far as possible).  
  - Logging of questions and responses (without PII) for review.  
  - Option to display source excerpts for transparency.

- **Outputs:**  
  - Natural-language answer, referencing underlying knowledge.  
  - Optional “snippets used” so the agent remains auditable.

#### Key Features

- Simple, browser-based chat-like interface via Streamlit.  
- RAG pattern: retrieval first, then answer generation.  
- Configurable knowledge base (point to different BFSI corpora).  
- Basic safeguards to avoid off-domain answers.  
- Can be used as an **internal agent** for staff or external for customers (with adaptations).

#### Example Workflow

1. Launch the service app and load a sample knowledge base.  
2. Enter questions such as “What is the dispute timeline for card chargebacks?”  
3. The agent retrieves relevant policy snippets and crafts an answer.  
4. User reads the answer and optionally inspects the referenced snippets.  
5. Governance or product teams review logs for tuning and quality.

#### Implementation Roadmap (Real BFSI)

- **Phase 1 – Internal Copilot**  
  - Start with internal agents (contact-center, back-office, branch staff).  
  - Use internal manuals and policy documents only.

- **Phase 2 – Harden & Govern**  
  - Add layered approval workflows for knowledge updates.  
  - Introduce guardrails for sensitive topics (complaints, legal, disputes).  
  - Build feedback loops and red-teaming processes.

- **Phase 3 – External Self-Service**  
  - Embed into mobile/web banking as a customer-facing assistant.  
  - Integrate with authentication and personalization (while respecting privacy).  
  - Measure impact on call deflections, CSAT, and containment rates.

#### Indicative ROI & KPIs

- Reduction in **basic inquiry volumes** to call centers.  
- Higher FCR for standard queries.  
- Shorter average handling time (AHT) for complex calls when used as an internal copilot.  
- Improved consistency and regulatory alignment of responses.

---

### 4. Compliance Monitoring Agent

#### Overview

The **Compliance Monitoring Agent** provides a **rule-based first-line check** on transactional or customer data against basic policy/regulatory rules. It is not a full AML/KYC system but a **teachable demo** for how AI-assisted rules and analytics can augment compliance work.

#### Problem Statement

- Regulatory expectations are expanding (KYC, AML, sanctions, conduct risk).  
- Many first-line checks are **manual and spreadsheet-driven**.  
- Evidence for audits is often **scattered and difficult to trace**.  

#### Solution Architecture

- **Inputs (demo):**  
  - CSV representing customers, transactions, or activities with relevant attributes (e.g., country, risk rating, product type, PEP flag, etc.).

- **Core Logic (illustrative):**  
  - Configurable rules engine (e.g., if high-risk country + high value + new customer → flag).  
  - Optional scoring of compliance risk (aggregation of rule hits).  
  - Simple summarization of flagged records.

- **Guardrails:**  
  - Explicitly demo-level rules, not comprehensive AML frameworks.  
  - Pseudonymization of direct identifiers.  
  - Logging of rule hits and configurations for audit.

- **Outputs:**  
  - List of flagged records and corresponding rules triggered.  
  - Summary metrics (# flags by rule, by segment).

#### Key Features

- CSV upload and quick rule evaluation from the UI.  
- Human-readable rule definitions for easier review and modification.  
- Summary dashboards showing concentration of compliance risk.  
- Hooks to add more advanced checks or plug into external screening systems (sanctions lists, watchlists, etc.).

#### Example Workflow

1. Upload a sample dataset of customers/transactions.  
2. Run the compliance checks and view flags.  
3. Drill into specific records and see which rules fired.  
4. Export flagged records for further investigation in existing compliance tools.

#### Implementation Roadmap (Real BFSI)

- **Phase 1 – Prototype & Education**  
  - Use synthetic/de-identified data to explore rule design with compliance teams.  

- **Phase 2 – Integration with Existing Stack**  
  - Connect to KYC/AML systems and case management platforms.  
  - Add scheduling to run checks regularly (e.g., daily batches).

- **Phase 3 – Advanced Analytics & AI**  
  - Combine rule outputs with anomaly detection or graph-based analytics.  
  - Introduce explainable AI models for complex pattern detection.

#### Indicative ROI & KPIs

- Faster first-line checks and more structured evidence for audits.  
- Reduced reliance on ad-hoc spreadsheets.  
- Improved coverage and consistency of simple rule-based controls.

---

## Guardrails, Privacy, and Compliance

This repository is intentionally built to **demonstrate responsible AI concepts** in BFSI:

- **Input Validation**  
  - Basic schema checks on uploaded files (columns, data types, null handling).  
  - Constraints on file sizes to avoid overload and abuse.

- **PII Pseudonymization**  
  - Direct identifiers (e.g., customer IDs) are designed to be hashed or replaced with pseudonyms.  
  - Processing is intended to be **in-memory** for demo; no persistent storage of raw PII.

- **Logging & Observability**  
  - Focus on logging **metadata**, errors, and summary statistics rather than full PII payloads.  
  - A sample log file (`bfsi_logs.txt`) can be used in development to debug flows.

- **Simple Rate Limiting & Usage Controls**  
  - Basic mechanisms to avoid unlimited scoring or LLM calls from a single session.

### Alignment with Key Regulations (Conceptual)

The repo **does not claim full compliance** with any regulation, but the patterns map conceptually to:

- **GDPR / PIPEDA:**  
  - Data minimization, pseudonymization, purpose limitation, transparency.  
- **PCI-DSS (for payments data):**  
  - Avoidance of storing full PAN or sensitive authentication data.  
- **KYC/AML & Financial Crime:**  
  - Basic examples of rule-based checks and documentation of findings.  

> **Important:** This is only conceptual guidance. Any real-world deployment must be reviewed and approved by your **Legal, Compliance, Security, Data Protection, and Model Risk** functions.

---

## Getting Started (Quickstart)

### Prerequisites

- **Python:** 3.x (e.g., 3.9+ recommended)  
- **System Tools:**  
  - Git  
  - Virtual environment tool of your choice (`venv`, `conda`, etc.)  

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/mohankhilariwal/bfsi-ai-agents-repo.git
cd bfsi-ai-agents-repo

# 2. Create and activate a virtual environment (example with venv)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scriptsctivate

# 3. Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file at the project root (if not already present).  
2. Set any required keys/variables, for example:

   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   # Add other provider keys or configuration values as needed
   ```

3. For local-only experiments, you can adapt the agents to use local models or rule-based logic without external APIs.

---

## Running the Agents

From the project root (with the virtual environment activated):

```bash
# Fraud Detection Agent
streamlit run fraud_app.py

# Credit Risk Assessment Agent
streamlit run credit_app.py

# Customer Service / BFSI Support Agent
streamlit run service_app.py

# Compliance Monitoring Agent
streamlit run compliance_app.py
```

### Sample Data

- Demo CSVs are located under the `data/` directory (e.g., transactions, applications, FAQs, etc.).  
- In most apps you can **either**:
  - Use the default sample file preloaded by the app, **or**  
  - Upload your own CSV with a compatible schema.

---

## Extending & Customizing

This repo is designed as a **starting point**. Typical extensions include:

- **Model Customization**  
  - Replace placeholder models with your institution’s **production-grade** fraud and credit risk models.  
  - Integrate with your MLOps platform for versioning, monitoring, and retraining.

- **Data Integration**  
  - Connect to internal data warehouses (e.g., Snowflake, BigQuery, on-prem DWH).  
  - Use secure internal APIs or message buses for real-time data.

- **LLM & RAG Enhancements**  
  - Swap LLM provider/model and tune prompts.  
  - Use advanced retrieval strategies (dense + sparse, re-ranking, etc.).  
  - Add role-based access control and personalization for the service agent.

- **Guardrail Hardening**  
  - Implement more robust input sanitization.  
  - Add policy engines (e.g., for content filtering or access control).  
  - Introduce detailed audit logs with proper retention and access policies.

- **Operationalization**  
  - Containerize the apps with Docker.  
  - Deploy behind API gateways and institutional SSO.  
  - Integrate with existing monitoring, logging (SIEM), and incident-management tools.

---

## Roadmap & Future Ideas

Potential future enhancements for this repo include:

- **Fraud & Credit**  
  - More advanced feature engineering and explainable ML models.  
  - Multi-product, multi-country support with configurable strategies.  

- **Service & Compliance**  
  - Richer conversational flows and multi-turn RAG.  
  - Integration with sanctions/PEP screening providers (conceptual demo).  

- **Multi-Agent Orchestration**  
  - Agents that collaborate (e.g., fraud agent triggering compliance checks).  
  - Workflow orchestration engines with human-in-the-loop approvals.

- **MLOps & Governance Modules**  
  - Model performance dashboards, drift detection, alerting.  
  - Fairness/bias and explainability reports.  
  - Template documentation aligned to model risk management standards.

---

## Limitations & Disclaimer

- This repository is a **demo and learning resource only**.  
- It is **not production-ready software** and **not** a complete fraud, credit, service, or AML system.  
- Any ROI or performance numbers mentioned are **illustrative only**, not promises or guarantees.  
- The sample data is synthetic/demo and **not representative** of real customer populations.  
- Any real-world BFSI deployment must go through:  
  - Security reviews  
  - Data protection / privacy impact assessments  
  - Compliance & legal sign-off  
  - Model risk and validation processes  

Use this repo as a **conceptual and technical reference**, not as a drop-in replacement for enterprise platforms.

---

## License & Attribution

- **License:** (TBD – update this section once a license is chosen, e.g., MIT, Apache 2.0).  
- **Author:** Maintained by *Mohan Khilariwal* as part of a broader portfolio of **BFSI AI proof-of-concepts and agentic AI experiments**.  

If you use or extend this work, consider referencing this repo and sharing improvements back with the community.
