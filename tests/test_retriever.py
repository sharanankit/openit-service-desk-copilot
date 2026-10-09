
import numpy as np
import pytest

from src.openit_copilot.retriever import cosine_similarity


def test_identical_vectors_have_similarity_one():
    vector = np.array([1.0, 2.0, 3.0])
    score = cosine_similarity(vector, vector.reshape(1, -1))

    assert score[0] == pytest.approx(1.0)


def test_orthogonal_vectors_have_similarity_zero():
    query = np.array([1.0, 0.0])
    vectors = np.array([
        [0.0, 1.0],
        [1.0, 0.0],
    ])

    scores = cosine_similarity(query, vectors)

    assert scores[0] == pytest.approx(0.0)
    assert scores[1] == pytest.approx(1.0)


def test_zero_vector_is_rejected():
    query = np.array([0.0, 0.0])
    vectors = np.array([[1.0, 0.0]])

    with pytest.raises(ValueError, match="zero vectors"):
        cosine_similarity(query, vectors)
