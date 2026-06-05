import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def test_client():
    """Provide a shared test client for the FastAPI app."""
    return TestClient(app)
