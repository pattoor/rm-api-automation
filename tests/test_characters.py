import pytest
from services.rm_client import RMClient
from models.character import Character, Location, Episode

client = RMClient()

# --- CHARACTER TESTS ---

def test_get_rick_success():
    """1. Basic Success Test: Retrieve Rick Sanchez (ID 1)"""
    response = client.get_character(1)
    print(response.json()["name"])  # Rick Sanchez
    assert response.status_code == 200
    assert response.json()["name"] == "Rick Sanchez"

def test_character_schema_validation():
    """2. Schema Test: Validate that the data conforms to the model"""
    data = client.get_character(2).json()
    # If the structure fails, Pydantic will raise an error here
    assert Character(**data)

@pytest.mark.parametrize("char_id", [1, 2, 3])
def test_multiple_characters(char_id):
    """3, 4, 5. Parameterized Test: Test IDs 1, 2, and 3"""
    response = client.get_character(char_id)
    assert response.status_code == 200
    assert response.json()["id"] == char_id

def test_character_not_found():
    """6. Negative Test: Validate a 404 error for a non-existent character"""
    response = client.get_character(9999)
    assert response.status_code == 404
    assert "error" in response.json()

# --- LOCATION TESTS ---

def test_get_location_success():
    """7. Location Test: Validate Earth (ID 1)"""
    response = client.get_location(1)
    data = response.json()
    assert response.status_code == 200
    assert Location(**data)
    assert data["name"] == "Earth (C-137)"

def test_location_invalid_format():
    """8. Negative Test: Validate that a text ID returns error 400 or 500"""
    response = client.get_location("abc")
    # The Rick & Morty API often responds with 500 for malformed IDs
    assert response.status_code in [400, 500] # Server or client error

# --- EPISODE TESTS ---

def test_get_episode_success():
    """9. Episode Test: Validate the first episode"""
    response = client.get_episode(1)
    data = response.json()
    assert response.status_code == 200
    # Validate that the episode code follows the SxxExx format
    assert data["episode"].startswith("S01")
    assert Episode(**data)

def test_episode_data_integrity():
    """10. Integrity Test: Validate that the air_date field is present and non-empty"""
    response = client.get_episode(1)
    assert len(response.json()["air_date"]) > 0 