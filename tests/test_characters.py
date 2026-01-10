import pytest
from services.rm_client import RMClient
from models.character import Character, Location, Episode

client = RMClient()

# --- TESTS DE PERSONAJES ---

def test_get_rick_success():
    """1. Test básico de éxito: Obtener a Rick Sanchez (ID 1)"""
    response = client.get_character(1)
    print(response.json()["name"]) # Rick Sanchez
    assert response.status_code == 200
    assert response.json()["name"] == "Rick Sanchez"

def test_character_schema_validation():
    """2. Test de Esquema: Validar que la data cumple con el modelo Pydantic"""
    data = client.get_character(2).json()
    # Si falla la estructura, Pydantic lanzará un error aquí
    assert Character(**data)

@pytest.mark.parametrize("char_id", [1, 2, 3])
def test_multiple_characters(char_id):
    """3, 4, 5. Test Parametrizado: Probar IDs 1, 2 y 3 en una sola función"""
    response = client.get_character(char_id)
    assert response.status_code == 200
    assert response.json()["id"] == char_id

def test_character_not_found():
    """6. Test Negativo: Validar error 404 para un personaje que no existe"""
    response = client.get_character(9999)
    assert response.status_code == 404
    assert "error" in response.json()

# --- TESTS DE UBICACIONES (LOCATIONS) ---

def test_get_location_success():
    """7. Test de Ubicación: Validar la Tierra (ID 1)"""
    response = client.get_location(1)
    data = response.json()
    assert response.status_code == 200
    assert Location(**data)
    assert data["name"] == "Earth (C-137)"

def test_location_invalid_format():
    """8. Test Negativo: Validar que un ID de texto da error 500 o 400"""
    response = client.get_location("abc")
    # La API de Rick & Morty suele responder 500 para IDs mal formateados
    assert response.status_code in [400, 500]

# --- TESTS DE EPISODIOS (EPISODES) ---

def test_get_episode_success():
    """9. Test de Episodio: Validar el primer episodio"""
    response = client.get_episode(1)
    data = response.json()
    assert response.status_code == 200
    # Validamos que el código de episodio tenga el formato correcto SxxExx
    assert data["episode"].startswith("S01")
    assert Episode(**data)

def test_episode_data_integrity():
    """10. Test de Integridad: Validar que el campo air_date no esté vacío"""
    response = client.get_episode(1)
    assert len(response.json()["air_date"]) > 0