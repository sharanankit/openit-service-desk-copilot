# OpenIT Service Desk Copilot — Architecture

1. Overview

OpenIT Service Desk Copilot uses Retrieval-Augmented Generation (RAG) to answer IT troubleshooting questions using a collection of approved knowledge documents.

The architecture separates document ingestion, retrieval, answer generation, and evaluation so that each component can be tested independently.

2. Logical Architecture


flowchart TD
    A[IT Runbooks and FAQs] --> B[Document Ingestion]
    B --> C[Text Cleaning and Chunking]
    C --> D[Embedding Generation]
    D --> E[Knowledge Index]

    F[User Question] --> G[Query Embedding]
    G --> H[Similarity Search]
    E --> H

    H --> I[Top-K Retrieved Passages]
    I --> J[Evidence and Relevance Checks]
    J --> K[Gemini Answer Generation]
    K --> L[Answer with Source References]

    M[Evaluation Dataset] --> N[Retrieval and Answer Evaluation]
    H --> N
    L --> N

## 3. Component Responsibilities

### Document Ingestion
Loads synthetic IT runbooks and FAQs from the project knowledge directory.

### Text Cleaning and Chunking
Extracts usable text and divides documents into smaller passages suitable for retrieval.

### Embedding Generation
Converts document passages and user questions into numerical vectors using an embedding model.

### Knowledge Index
Stores passage text, document identifiers, metadata, and embeddings. The initial implementation may use an in-memory NumPy index.

### Retrieval
Compares the question embedding with indexed passage embeddings and ranks candidates using cosine similarity.

### Evidence and Relevance Checks
Determines whether the retrieved content is sufficiently relevant to be considered for answering. Any threshold must be calibrated using evaluation data.

### Answer Generation
Uses Gemini to generate a response grounded in the retrieved passages. The model is instructed to acknowledge insufficient evidence and provide source references.

### Evaluation
Measures retrieval quality, answer support, citation correctness, abstention behaviour, latency, and token usage where available.

## 4. Technology Choices

| Component | Initial choice | Rationale |
|---|---|---|
| Application language | Python | Readable, widely used for AI engineering |
| Language model | Gemini API | Cloud-based generation without requiring a large local model |
| Embedding model | gemini-embedding-001 | Generates vector representations of text |
| Similarity calculation | NumPy | Lightweight mathematical operations |
| Document parsing | pypdf and Python | Supports PDF text extraction and basic document processing |
| Testing | pytest | Automated verification of expected behaviour |
| Version control | Git and GitHub | Change tracking and public collaboration |

These are initial choices and may change if experiments demonstrate a better trade-off.

## 5. Request Flow

1. A user submits an IT troubleshooting question.
2. The system generates an embedding for the question.
3. Retrieval ranks passages in the knowledge index.
4. The system checks whether the retrieved evidence is adequate.
5. If evidence is insufficient, the system returns an explicit uncertainty response.
6. Otherwise, the selected passages are supplied to Gemini as context.
7. The application returns the answer with source references.
8. Evaluation instrumentation records relevant quality and performance metrics.

## 6. Security and Trust Boundaries

- API credentials are supplied through environment configuration and must not be committed.
- The public repository uses synthetic documentation.
- Retrieved passages are treated as untrusted data and