# services/rm_client.py
import requests

class RMClient:
    def __init__(self):
        self.BASE_URL = "https://rickandmortyapi.com/api"

    def get_character(self, char_id: int):
        response = requests.get(f"{self.BASE_URL}/character/{char_id}")
        return response 

    def get_location(self, loc_id):
        return requests.get(f"{self.BASE_URL}/location/{loc_id}")

    def get_episode(self, ep_id):
        return requests.get(f"{self.BASE_URL}/episode/{ep_id}")
    