class Match:
    """
    Modèle représentant un match entre deux joueurs.
    """

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = None
        self.score_2 = None

    def set_result(self, score_1: float, score_2: float) -> None:
        valid_results = [(1, 0), (0, 1), (0.5, 0.5)]
        if (score_1, score_2) not in valid_results:
            raise ValueError("Résultat invalide.")

        self.score_1 = score_1
        self.score_2 = score_2

        self.player_1.add_score(score_1)
        self.player_2.add_score(score_2)

    def to_tuple(self):
        """
        Format exigé par les spécifications techniques.
        """
        return (
            [self.player_1.national_id, self.score_1],
            [self.player_2.national_id, self.score_2],
        )
