"""Modèle représentant un match entre deux joueurs."""


class Match:
    """Représente un match avec deux joueurs et leurs scores."""

    def __init__(self, player_1, player_2):
        """Initialise un match entre deux joueurs."""
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = None
        self.score_2 = None

    def set_result(self, score_1: float, score_2: float) -> None:
        """Enregistre le résultat du match et met à jour les scores des joueurs."""
        valid_results = [(1, 0), (0, 1), (0.5, 0.5)]
        if (score_1, score_2) not in valid_results:
            raise ValueError("Résultat invalide.")
        self.score_1 = score_1
        self.score_2 = score_2
        self.player_1.add_score(score_1)
        self.player_2.add_score(score_2)

    def to_tuple(self) -> tuple:
        """Retourne le match sous forme de tuple de listes [joueur, score]."""
        return (
            [self.player_1.national_id, self.score_1],
            [self.player_2.national_id, self.score_2],
        )

    def to_dict(self) -> dict:
        """Sérialise le match en dictionnaire."""
        return {
            "player_1": self.player_1.to_dict(),
            "player_2": self.player_2.to_dict(),
            "score_1": self.score_1,
            "score_2": self.score_2,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Match":
        """Crée un match à partir d'un dictionnaire."""
        from models.player import Player

        player_1 = Player.from_dict(data["player_1"])
        player_2 = Player.from_dict(data["player_2"])
        match = cls(player_1, player_2)
        match.score_1 = data["score_1"]
        match.score_2 = data["score_2"]
        return match
