class TennisGame:
    def __init__(self, first_player_name, second_player_name):
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.first_player_score = 0
        self.second_player_score = 0

    def won_point(self, player_name):
        if self.first_player_name == player_name:
            self.first_player_score += 1
        else:
            self.second_player_score += 1

    def _get_score_name(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"

    def _get_tied_score(self):
        if self.first_player_score < 4:
            score = self._get_score_name(self.first_player_score)
            return f"{score}-All"
        else:
            return "Deuce"
    
    def _get_deuce_score(self):
        score_difference = self.first_player_score - self.second_player_score

        if score_difference == 1:
            return f"Advantage {self.first_player_name}"
        elif score_difference == -1:
            return f"Advantage {self.second_player_name}"
        elif score_difference >= 2:
            return f"Win for {self.first_player_name}"
        else:
            return f"Win for {self.second_player_name}"
    
    def get_score(self):
        if self.second_player_score == self.first_player_score:
            return self._get_tied_score()
        elif self.first_player_score >= 4 or self.second_player_score >= 4:
            return self._get_deuce_score()
        else:
            score = self._get_score_name(self.first_player_score)
            score += "-" + self._get_score_name(self.second_player_score)
            return score
