# OpenIT Service Desk Copilot

**An evidence-grounded AI assistant for IT support teams.**

OpenIT Copilot is an AI engineering project exploring how IT support teams can find troubleshooting guidance faster, answer technical questions using approved documentation, and prepare better incident handovers.

The initial implementation focuses on document ingestion, text chunking, embedding generation, and semantic retrieval. The product roadmap aims to extend this foundation into a practical IT knowledge assistant with source-cited answers, guided troubleshooting, and incident-ticket drafting.

> **Project status:** Early prototype. Retrieval is implemented and basic unit tests pass. Answer generation, a user interface, and production integrations are planned—not yet implemented.

## The Problem

IT support teams often rely on troubleshooting runbooks, internal knowledge articles, and technical documentation to resolve recurring incidents.

Finding the right procedure can take time. Inconsistent troubleshooting and incomplete ticket notes can also make incident resolution and escalation harder.

OpenIT Copilot explores a practical solution: retrieve relevant knowledge from approved documents and use that evidence to help support analysts investigate issues more consistently.

## Proposed Solution

The long-term product vision is to help IT support teams:

- Search technical documentation using natural-language questions.
- Receive answers supported by relevant source passages.
- Follow documented troubleshooting procedures.
- Prepare structured incident summaries and handover notes.
- Identify questions that the existing knowledge base cannot answer.

These are planned capabilities unless explicitly identified as implemented below.

## Current Capabilities

The current prototype includes:

- **Markdown document loading:** Reads sample IT support runbooks.
- **Text chunking:** Splits documents into overlapping text segments.
- **Embedding generation:** Uses Google's Gemini embedding model.
- **Semantic retrieval:** Uses vector similarity to retrieve relevant text chunks.
- **Unit tests:** Tests cosine similarity calculations and zero-vector handling.

The sample knowledge base contains three synthetic runbooks:

1. VPN troubleshooting
2. Password reset
3. Software installation

An initial forgotten-password query retrieved `password_reset.md` as its top result.

## Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| Embeddings | Google Gemini API |
| Vector operations | NumPy |
| Source documents | Markdown |
| Testing | pytest |
| Version control | Git and GitHub |

The current retriever uses in-memory vector storage. A persistent vector database and production deployment have not yet been implemented.

## Architecture

The current retrieval pipeline follows this flow:

1. Load Markdown runbooks.
2. Split documents into overlapping chunks.
3. Generate embeddings for the chunks.
4. Compare a query embedding with stored chunk embeddings.
5. Return the most similar chunks and their source metadata.

The planned next stage is to pass retrieved evidence to a language model for grounded answer generation, with source citations and explicit handling of insufficient evidence.

## Getting Started

### Prerequisites

- Python 3.13 or a compatible Python version
- Git
- A Google Gemini API key

### Setup

Clone the repository:

```bash
git clone https://github.com/sharanankit/openit-service-desk-copilot.git
cd openit-service-desk-copilot
```

Create and activate a virtual environment on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Set your Gemini API key in the terminal:

```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your own key. Never commit API keys or other credentials to GitHub.

Run the existing tests:

```bash
python -m pytest tests/test_retriever.py -v
```

Run the document loader:

```bash
python -m src.openit_copilot.document_loader
```

Run the chunker:

```bash
python -m src.openit_copilot.chunker
```

Run the retriever:

```bash
python -m src.openit_copilot.retriever
```

The retriever requires a valid Gemini API key and API access. API usage may incur charges depending on your account and current pricing.

## Commercial Direction

The initial business hypothesis is to offer small IT support companies and managed service providers a narrowly scoped AI knowledge-assistant pilot.

Potential services include:

- Configuration of an assistant over approved knowledge documents.
- Evaluation of retrieval quality and source relevance.
- Setup documentation and handover.
- Optional ongoing maintenance and knowledge-base improvements.

The initial goal is to validate whether customers will pay for this solution before investing in a larger SaaS platform.

Pricing, customer demand, and recurring revenue are not yet validated.

## Roadmap

- [x] Create the initial Python project and sample runbooks.
- [x] Implement document loading and text chunking.
- [x] Implement Gemini embeddings and similarity-based retrieval.
- [x] Add initial unit tests.
- [ ] Implement evidence-grounded answer generation.
- [ ] Add source citations and insufficient-evidence handling.
- [ ] Build a lightweight user interface.
- [ ] Create a representative evaluation dataset.
- [ ] Add guided troubleshooting and incident-ticket drafting.
- [ ] Validate the solution with prospective customers.
- [ ] Develop a repeatable implementation and support offering.

## Security and Limitations

This prototype uses synthetic sample runbooks and is not a production IT support system.

It does not currently execute remediation commands, connect to live IT service-management systems, or provide autonomous incident resolution.

Before using real customer documents, the deployment must address data privacy, access permissions, credential handling, logging, and the customer's security requirements.

AI-generated guidance must be evaluated before operational use. Human review remains necessary for consequential troubleshooting and incident actions.

## Contributing

This project is being developed incrementally. Suggestions, issue reports, and feedback on practical IT support use cases are welcome.

## License

The repository's license should be confirmed before external reuse or commercial distribution.
