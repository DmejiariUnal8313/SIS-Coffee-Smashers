import requests
import json
import pandas as pd

class StartGGApplication:
    def __init__(self):
        self.base_url = 'https://api.start.gg/gql/alpha'

    def get_player_info(self, player_id):
        response = requests.get(f'{self.base_url}/players/{player_id}')
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_tournament_info(self, tournament_id):
        response = requests.get(f'{self.base_url}/tournaments/{tournament_id}')
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_ranking(self, tournament_id):
        response = requests.get(f'{self.base_url}/tournaments/{tournament_id}/ranking')
        if response.status_code == 200:
            return response.json()
        else:
            return None

app = StartGGApplication()
player_info = app.get_player_info('player_id')
tournament_info = app.get_tournament_info('tournament_id')
ranking = app.get_ranking('tournament_id')

print(player_info)
print(tournament_info)
print(ranking)
    