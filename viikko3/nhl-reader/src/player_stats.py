class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
        
    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()
        by_nationality = filter(lambda p: p.nationality == nationality, players)
        return sorted(by_nationality, key=lambda p: p.total_points, reverse=True)