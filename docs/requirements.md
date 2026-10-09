# OpenIT Service Desk Copilot — Requirements

## 1. Purpose

Define the functional and non-functional requirements for the OpenIT Service Desk Copilot.

## 2. Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Accept an IT troubleshooting question in natural language. | Must |
| FR-02 | Load and process synthetic IT knowledge documents. | Must |
| FR-03 | Generate embeddings for document passages and user questions. | Must |
| FR-04 | Retrieve and rank the most relevant passages. | Must |
| FR-05 | Generate troubleshooting guidance using retrieved evidence. | Must |
| FR-06 | Provide references to the source documents supporting the answer. | Must |
| FR-07 | Acknowledge when retrieved evidence is insufficient. | Must |
| FR-08 | Measure retrieval quality using a labelled evaluation dataset. | Must |
| FR-09 | Record response latency and token usage where available. | Must |
| FR-10 | Provide a simple interface for testing questions. | Should |
| FR-11 | Run automated tests for retrieval and answer behaviour. | Must |

## 3. Non-Functional Requirements

### Security
- Never commit API keys or other secrets.
- Use synthetic knowledge documents in the public repository.
- Do not execute commands on enterprise systems.
- Treat retrieved documents as data, not as instructions to override system safeguards.

### Reliability
- Handle empty queries and missing configuration gracefully.
- Handle API errors without exposing credentials.
- Avoid presenting unsupported procedures as verified facts.

### Maintainability
- Separate document processing, retrieval, answer generation, and evaluation logic.
- Use readable Python modules and meaningful function names.
- Document setup, configuration, execution, and known limitations.

### Reproducibility
- Document Python and dependency requirements.
- Provide a repeatable evaluation procedure.
- Record the model and relevant configuration used for each evaluation run.

### Performance
- Measure latency on a representative set of questions.
- Track token usage where the API exposes it.
- Establish performance baselines before defining optimization targets.

## 4. Evaluation Requirements

The evaluation dataset should include:

1. Questions with clearly relevant supporting documents.
2. Questions that require matching different wording with similar meaning.
3. Questions with multiple potentially relevant passages.
4. Questions for which the knowledge base contains no adequate answer.
5. Questions involving ambiguous or incomplete information.

Retrieval evaluation must compare returned documents against manually labelled relevant documents.

Answer evaluation must assess factual support, citation correctness, completeness, and appropriate abstention.

## 5. Acceptance Criteria

The initial release is acceptable when:

- The application retrieves relevant passages for supported test queries.
- Generated answers cite the supporting documents.
- Unsupported questions receive an explicit insufficient-evidence response.
- Automated tests cover core retrieval and error-handling behaviour.
- Evaluation results and known limitations are documented.
- A developer can reproduce the documented setup using their own API key.

These are acceptance requirements, not claims that the implementation has already passed them.