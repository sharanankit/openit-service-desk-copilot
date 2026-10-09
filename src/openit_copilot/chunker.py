
from typing import Any


def chunk_document(
    document: dict[str, Any],
    chunk_size: int = 500,
    overlap: int = 100,
) -> list[dict[str, Any]]:
    """Split a document into overlapping character-based chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and < chunk_size.")

    text = document["text"].strip()
    if not text:
        return []

    chunks = []
    start = 0
    chunk_number = 0
    step = chunk_size - overlap

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk_text = text[start:end].strip()

        if chunk_text:
            chunks.append({
                "chunk_id": f"{document['document_id']}_chunk_{chunk_number}",
                "document_id": document["document_id"],
                "source": document["source"],
                "text": chunk_text,
                "start_char": start,
                "end_char": end,
            })
            chunk_number += 1

        start += step

    return chunks


if __name__ == "__main__":
    from src.openit_copilot.document_loader import load_markdown_documents

    documents = load_markdown_documents("data/sample_runbooks")
    all_chunks = []

    for document in documents:
        all_chunks.extend(chunk_document(document))

    print(f"Documents loaded: {len(documents)}")
    print(f"Chunks created: {len(all_chunks)}\n")

    for chunk in all_chunks:
        print(f"Chunk ID: {chunk['chunk_id']}")
        print(f"Source: {chunk['source']}")
        print(f"Characters: {len(chunk['text'])}")
        print(f"Preview: {chunk['text'][:100]}...")
        print("-" * 40)
