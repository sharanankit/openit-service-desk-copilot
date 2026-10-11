
import pytest

from src.openit_copilot.source_registry import (
    find_source_for_url,
    validate_document_metadata,
)


@pytest.fixture
def registry():
    return {
        "policy": {"official_sources_only": True},
        "sources": [
            {
                "id": "microsoft_learn",
                "vendor": "Microsoft",
                "name": "Microsoft Learn",
                "base_url": "https://learn.microsoft.com/",
                "approval_status": "approved",
                "enabled": True,
            },
            {
                "id": "microsoft_troubleshoot",
                "vendor": "Microsoft",
                "name": "Microsoft Troubleshooting",
                "base_url": "https://learn.microsoft.com/en-us/troubleshoot/",
                "approval_status": "approved",
                "enabled": True,
            },
            {
                "id": "salesforce_help",
                "vendor": "Salesforce",
                "name": "Salesforce Help",
                "base_url": "https://help.salesforce.com/",
                "approval_status": "pending_terms_review",
                "enabled": False,
            },
        ],
    }


def test_approved_official_url_is_accepted(registry):
    source = find_source_for_url(
        "https://learn.microsoft.com/en-us/azure/",
        registry,
    )
    assert source["id"] == "microsoft_learn"


def test_most_specific_source_path_is_selected(registry):
    source = find_source_for_url(
        "https://learn.microsoft.com/en-us/troubleshoot/",
        registry,
    )
    assert source["id"] == "microsoft_troubleshoot"


def test_lookalike_domain_is_rejected(registry):
    source = find_source_for_url(
        "https://learn.microsoft.com.unofficial-example.com/",
        registry,
    )
    assert source is None


def test_unapproved_source_is_rejected(registry):
    source = find_source_for_url(
        "https://help.salesforce.com/",
        registry,
    )
    assert source is None


def test_http_url_is_rejected(registry):
    source = find_source_for_url(
        "http://learn.microsoft.com/",
        registry,
    )
    assert source is None


def test_missing_document_title_is_rejected(registry):
    with pytest.raises(ValueError, match="title"):
        validate_document_metadata(
            {
                "canonical_url": "https://learn.microsoft.com/",
                "document_type": "troubleshooting",
            },
            registry,
        )


def test_valid_metadata_includes_source_provenance(registry):
    document = validate_document_metadata(
        {
            "title": "Example troubleshooting guide",
            "canonical_url": "https://learn.microsoft.com/en-us/azure/",
            "document_type": "troubleshooting",
        },
        registry,
    )

    assert document["vendor"] == "Microsoft"
    assert document["source_id"] == "microsoft_learn"
