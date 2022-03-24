import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url
    
    def get_players(self):
        player_json = requests.get(self._url).json()
        players = []
        for player_dict in player_json:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games'],
            )
            players.append(player)
        return players