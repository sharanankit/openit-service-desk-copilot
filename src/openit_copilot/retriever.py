
import os
from typing import Any

import numpy as np
from google import genai

from src.openit_copilot.chunker import chunk_document
from src.openit_copilot.document_loader import load_markdown_documents


EMBEDDING_MODEL = "gemini-embedding-001"


def cosine_similarity(query_vector: np.ndarray, vectors: np.ndarray) -> np.ndarray:
    """Calculate cosine similarity between one query vector and many vectors."""
    query_norm = np.linalg.norm(query_vector)
    vector_norms = np.linalg.norm(vectors, axis=1)

    if query_norm == 0 or np.any(vector_norms == 0):
        raise ValueError("Cannot calculate cosine similarity for zero vectors.")

    return (vectors @ query_vector) / (vector_norms * query_norm)


class SemanticRetriever:
    """Embed knowledge chunks and retrieve the most similar passages."""

    def __init__(self, client: Any):
        self.client = client
        self.chunks: list[dict[str, Any]] = []
        self.vectors: np.ndarray | None = None

    def index_documents(self, documents: list[dict[str, Any]]) -> None:
        """Chunk documents and create an in-memory embedding index."""
        self.chunks = []

        for document in documents:
            self.chunks.extend(chunk_document(document))

        if not self.chunks:
            self.vectors = None
            return

        response = self.client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=[chunk["text"] for chunk in self.chunks],
        )

        self.vectors = np.array(
            [embedding.values for embedding in response.embeddings],
            dtype=np.float32,
        )

    def search(self, query: str, top_k: int = 3) -> list[dict[str, Any]]:
        """Return the top-k chunks ranked by cosine similarity."""
        if not query.strip():
            raise ValueError("Query cannot be empty.")

        if top_k <= 0:
            raise ValueError("top_k must be positive.")

        if self.vectors is None or not self.chunks:
            return []

        response = self.client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=query,
        )

        query_vector = np.array(
            response.embeddings[0].values,
            dtype=np.float32,
        )

        scores = cosine_similarity(query_vector, self.vectors)
        ranked_indices = np.argsort(scores)[::-1][:top_k]

        return [
            {
                **self.chunks[int(index)],
                "similarity": float(scores[index]),
            }
            for index in ranked_indices
        ]


if __name__ == "__main__":
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing.")

    client = genai.Client(api_key=api_key)
    documents = load_markdown_documents("data/sample_runbooks")

    retriever = SemanticRetriever(client)
    retriever.index_documents(documents)

    query = "How can I recover my forgotten password?"
    results = retriever.search(query, top_k=3)

    print(f"Question: {query}\n")
    print(f"Documents indexed: {len(documents)}")
    print(f"Chunks indexed: {len(retriever.chunks)}\n")

    for rank, result in enumerate(results, start=1):
        print(f"{rank}. Similarity: {result['similarity']:.4f}")
        print(f"   Source: {result['source']}")
        print(f"   Chunk: {result['chunk_id']}")
        print(f"   Text: {result['text'][:200]}...")
        print()
