# OpenIT Copilot — Initial Evaluation Report

## 1. Evaluation Status

**Stage:** Initial semantic retrieval and unit testing  
**Environment:** Python 3.13 virtual environment on macOS  
**Embedding model:** gemini-embedding-001  
**Test framework:** pytest

## 2. Knowledge Base

| Metric | Observed result |
|---|---:|
| Synthetic runbook documents | 3 |
| Character-based chunks | 13 |
| Chunk size | 500 characters |
| Chunk overlap | 100 characters |

## 3. Retrieval Experiment

**Query:** How can I recover my forgotten password?

**Observed top result:**
- Source: `password_reset.md`
- Chunk: `password_reset_chunk_0`
- Cosine similarity: 0.6663

The top-ranked source matches the expected password-reset topic. This is an initial qualitative observation, not a comprehensive retrieval-quality measurement.

## 4. Automated Unit Tests

| Test | Result |
|---|---|
| Identical vectors have similarity 1 | PASS |
| Orthogonal vectors have similarity 0 | PASS |
| Zero vectors are rejected | PASS |

**Observed test run:** 3 passed in 1.75 seconds.

## 5. Current Capabilities

- Loads Markdown knowledge documents.
- Splits documents into overlapping character-based chunks.
- Generates embeddings through the Gemini API.
- Ranks passages using cosine similarity.
- Runs unit tests for core similarity calculations.

## 6. Not Yet Implemented

- Gemini-generated answers grounded in retrieved passages
- Source citations in generated answers
- Calibrated relevance thresholds and insufficient-evidence handling
- A labelled retrieval evaluation dataset
- Systematic latency and token-usage evaluation
- User interface and production ITSM integration

## 7. Next Evaluation Goals

1. Test queries from each runbook category.
2. Measure whether the expected document appears in the top-k results.
3. Add questions that the knowledge base cannot answer.
4. Evaluate answer grounding and citation correctness after generation is implemented.
5. Record measurements across multiple representative queries.