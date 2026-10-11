
"""Load and validate the official-source registry."""

import json
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_REGISTRY = Path("config/source_registry.json")


def load_registry(path: str | Path = DEFAULT_REGISTRY) -> dict:
    """Load the registry and validate its basic structure."""
    with Path(path).open("r", encoding="utf-8") as file:
        registry = json.load(file)

    if registry.get("policy", {}).get("official_sources_only") is not True:
        raise ValueError("Official-sources-only policy must be enabled.")

    sources = registry.get("sources")
    if not isinstance(sources, list):
        raise ValueError("Registry must contain a sources list.")

    seen_ids = set()

    for source in sources:
        if not isinstance(source, dict):
            raise ValueError("Each registered source must be an object.")

        for field in ("id", "vendor", "name", "base_url", "approval_status"):
            if not source.get(field):
                raise ValueError(f"Source is missing required field: {field}")

        if source["id"] in seen_ids:
            raise ValueError(f"Duplicate source ID: {source['id']}")
        seen_ids.add(source["id"])

        parsed = urlparse(source["base_url"])
        if (
            parsed.scheme != "https"
            or not parsed.hostname
            or parsed.username
            or parsed.password
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError(
                f"Source must have a valid HTTPS base URL: {source['id']}"
            )

        if source.get("enabled") is True and source["approval_status"] != "approved":
            raise ValueError(
                f"Source {source['id']} is enabled without approval."
            )

    return registry



def find_source_for_url(url: str, registry: dict) -> dict | None:
    """Find the most specific enabled, approved source matching a URL."""
    parsed_url = urlparse(url)

    if (
        parsed_url.scheme != "https"
        or not parsed_url.hostname
        or parsed_url.username
        or parsed_url.password
    ):
        return None

    hostname = parsed_url.hostname.lower()
    requested_path = parsed_url.path.rstrip("/") or "/"
    matches = []

    for source in registry["sources"]:
        parsed_base = urlparse(source["base_url"])
        registered_host = parsed_base.hostname

        if not registered_host:
            continue

        registered_host = registered_host.lower()

        if hostname != registered_host and not hostname.endswith(
            "." + registered_host
        ):
            continue

        base_path = parsed_base.path.rstrip("/") or "/"

        if base_path != "/":
            if requested_path != base_path and not requested_path.startswith(
                base_path + "/"
            ):
                continue

        if source.get("enabled") is not True:
            continue

        if source.get("approval_status") != "approved":
            continue

        matches.append((len(base_path), source))

    if not matches:
        return None

    matches.sort(key=lambda item: item[0], reverse=True)
    return matches[0][1]



def validate_document_metadata(document: dict, registry: dict) -> dict:
    """Validate provenance fields before a document enters the knowledge base."""
    required_fields = ("title", "canonical_url", "document_type")

    for field in required_fields:
        if not isinstance(document.get(field), str) or not document[field].strip():
            raise ValueError(f"Document is missing required field: {field}")

    source = find_source_for_url(document["canonical_url"], registry)

    if source is None:
        raise ValueError(
            "Document URL does not belong to an enabled, approved source."
        )

    return {
        **document,
        "vendor": source["vendor"],
        "source_id": source["id"],
    }


if __name__ == "__main__":
    registry = load_registry()
    print(f"Loaded {len(registry['sources'])} registered sources.")

    for source in registry["sources"]:
        print(
            f"- {source['vendor']}: {source['name']} "
            f"(enabled={source.get('enabled', False)})"
        )
