# OpenIT Service Desk Copilot — Problem Statement

## 1. Project Overview

OpenIT Service Desk Copilot is an open-source, evidence-grounded AI assistant designed to help IT service desk analysts find troubleshooting guidance from technical documentation.

The project demonstrates how Retrieval-Augmented Generation (RAG), semantic search, and source citations can support IT incident resolution.

This is a portfolio and learning project using synthetic documentation. It is not connected to a live enterprise ITSM platform.

## 2. Problem

IT support teams frequently handle recurring incidents involving password resets, VPN connectivity, software installation, access permissions, and device troubleshooting.

Relevant guidance may be distributed across knowledge articles, FAQs, and technical runbooks. Analysts may need to search several documents before finding an applicable procedure.

This can create avoidable search effort, inconsistent troubleshooting, and a risk of using outdated or irrelevant instructions.

## 3. Target Users

- Level 1 (L1) IT service desk analysts
- Level 2 (L2) IT support engineers
- IT knowledge management teams
- IT operations and service management leaders

## 4. Proposed Solution

Build a copilot that:

1. Accepts a natural-language IT incident question.
2. Searches a collection of approved, synthetic IT knowledge documents.
3. Retrieves the most relevant passages.
4. Generates troubleshooting guidance grounded in retrieved evidence.
5. Provides source references so users can verify the guidance.
6. Acknowledges when the available evidence is insufficient.
7. Records evaluation metrics to measure retrieval and answer quality.

## 5. Project Scope

### In scope

- Synthetic IT runbooks and FAQs
- Document ingestion and text processing
- Embedding generation and semantic retrieval
- Retrieval-Augmented Generation
- Source attribution
- Basic safeguards against unsupported answers
- Automated tests and a repeatable evaluation dataset
- Latency and token-usage measurements
- Public documentation and local execution instructions

### Out of scope for the initial version

- Integration with a live ServiceNow, Jira Service Management, or other ITSM instance
- Automatic execution of administrative commands
- Access to production systems
- Use of confidential company documents or real incident records
- Autonomous incident closure or changes to user permissions

## 6. Success Criteria

The project will be evaluated using a documented test dataset rather than anecdotal demonstrations.

Initial engineering targets:

- Every generated answer should provide source references when it relies on retrieved documentation.
- Unsupported questions should trigger an explicit uncertainty response rather than an invented troubleshooting procedure.
- Retrieval quality should be measured against manually identified relevant documents.
- Automated tests should cover normal queries, irrelevant queries, and insufficient-evidence cases.
- Latency and token usage should be recorded for representative test queries.
- A new developer should be able to follow the README and run the project using their own API credentials.

Numerical quality targets will be finalized after establishing a baseline on the evaluation dataset. They will not be presented as achieved results until measured.

## 7. Risks and Constraints

- Generated guidance may be inaccurate even when relevant documents are retrieved.
- Similarity scores do not guarantee relevance.
- Source documents may be incomplete or outdated.
- API availability, pricing, and rate limits may change.
- Public repository content must not contain API keys or confidential information.
- Human review remains necessary before high-impact operational actions.

## 8. Expected Outcome

The final deliverable will be a reproducible, documented,