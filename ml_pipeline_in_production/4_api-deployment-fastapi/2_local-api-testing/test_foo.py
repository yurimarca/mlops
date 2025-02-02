from fastapi.testclient import TestClient
from foo import app

# Initialize test client
client = TestClient(app)

def test_get_items_with_query():
    """Test GET request with item_id and count query parameter"""
    response = client.get("/items/42?count=3")
    assert response.status_code == 200
    assert response.json() == {"fetch": "Fetched 3 of 42"}

def test_get_items_without_query():
    """Test GET request with only item_id (count should default to 1)"""
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"fetch": "Fetched 1 of 42"}

def test_malformed_url():
    """Test a malformed request (non-integer item_id)"""
    response = client.get("/items")
    assert response.status_code != 200

def test_nonexistent_route():
    """Test an incorrect endpoint that doesn't exist"""
    response = client.get("/wrong_endpoint")
    assert response.status_code != 200
