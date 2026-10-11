from unittest.mock import Mock
from src.openit_copilot.answer_generator import generate_answer

def test_no_evidence_does_not_call_model():
    client = Mock()

    answer = generate_answer(client, "What is our VPN address?", [])

    assert "could not find relevant evidence" in answer.lower()
    client.models.generate_content.assert_not_called()


def test_empty_model_response_returns_fallback():
    from types import SimpleNamespace

    client = Mock()
    client.models.generate_content.return_value = SimpleNamespace(text=" ")
    chunks = [{
        "source": "vpn_troubleshooting.md",
        "chunk_id": "vpn_chunk_1",
        "text": "Restart the approved VPN application.",
    }]

    answer = generate_answer(client, "How do I troubleshoot VPN?", chunks)

    assert "could not generate a reliable answer" in answer.lower()


def test_prompt_contains_question_and_evidence():
    from types import SimpleNamespace

    client = Mock()
    client.models.generate_content.return_value = SimpleNamespace(
        text="Consult the IT support team."
    )
    chunks = [{
        "source": "vpn_troubleshooting.md",
        "chunk_id": "vpn_chunk_1",
        "text": "Restart the approved VPN application.",
    }]

    generate_answer(client, "How do I troubleshoot VPN access?", chunks)

    prompt = client.models.generate_content.call_args.kwargs["contents"]
    assert "How do I troubleshoot VPN access?" in prompt
    assert "vpn_troubleshooting.md" in prompt
    assert "vpn_chunk_1" in prompt
    assert "Restart the approved VPN application." in prompt
