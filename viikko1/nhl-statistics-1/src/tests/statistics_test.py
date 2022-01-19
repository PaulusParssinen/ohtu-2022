import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search_by_name_works(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")
    
    def test_search_by_invalid_name_return_none(self):
        player = self.statistics.search("huuhaa")
        self.assertIsNone(player)
        
    def test_team_search_works(self):
        team = self.statistics.team("EDM")
        self.assertEqual(len(team), 3)
        
    def test_get_single_top_scorer_correct(self):
        top_scorers = self.statistics.top_scorers(0)
        self.assertEqual(len(top_scorers), 1)
        self.assertEqual(top_scorers[0].name, "Gretzky")