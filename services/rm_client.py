"""Rick and Morty API client (simple Requests-based wrapper)."""
import requests


class RMClient:
    def __init__(self):
        self.BASE_URL = "https://rickandmortyapi.com/api"

    def get_character(self, char_id: int):
        """Retrieve a character by ID."""
        response = requests.get(f"{self.BASE_URL}/character/{char_id}")
        return response

    def get_location(self, loc_id):
        """Retrieve a location by ID."""
        return requests.get(f"{self.BASE_URL}/location/{loc_id}")

    def get_episode(self, ep_id):
        """Retrieve an episode by ID."""
        return requests.get(f"{self.BASE_URL}/episode/{ep_id}")
    