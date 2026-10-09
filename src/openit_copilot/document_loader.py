
from pathlib import Path


def load_markdown_documents(directory: str | Path) -> list[dict[str, str]]:
    """Load Markdown documents from a directory."""
    directory = Path(directory)

    if not directory.exists():
        raise FileNotFoundError(
            f"Knowledge directory not found: {directory}"
        )

    documents = []

    for file_path in sorted(directory.glob("*.md")):
        text = file_path.read_text(encoding="utf-8").strip()

        if not text:
            continue

        documents.append({
            "document_id": file_path.stem,
            "source": file_path.name,
            "text": text,
        })

    return documents


if __name__ == "__main__":
    knowledge_dir = Path("data/sample_runbooks")
    documents = load_markdown_documents(knowledge_dir)

    print(f"Loaded {len(documents)} documents\n")

    for document in documents:
        print(f"ID: {document['document_id']}")
        print(f"Source: {document['source']}")
        print(f"Characters: {len(document['text'])}")
        print("-" * 40)
