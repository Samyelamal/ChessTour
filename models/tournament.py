"""Modèle représentant un tournoi d'échecs."""

from models.player import Player
from models.round import Round


class Tournament:
    """Représente un tournoi avec ses joueurs, tours et métadonnées."""

    def __init__(
        self,
        name: str,
        location: str,
        start_date,
        end_date,
        number_of_rounds: int = 4,
        description: str = "",
    ):
        """Initialise un tournoi avec ses informations de base."""
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.players = []
        self.rounds = []
        self.current_round = 0

    def add_player(self, player) -> None:
        """Ajoute un joueur au tournoi."""
        self.players.append(player)

    def add_round(self, round_) -> None:
        """Ajoute un tour au tournoi et incrémente le compteur de tours."""
        self.rounds.append(round_)
        self.current_round += 1

    def to_dict(self) -> dict:
        """Sérialise le tournoi en dictionnaire."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "number_of_rounds": self.number_of_rounds,
            "description": self.description,
            "current_round": self.current_round,
            "players": [player.to_dict() for player in self.players],
            "rounds": [round_.to_dict() for round_ in self.rounds],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Tournament":
        """Crée un tournoi à partir d'un dictionnaire."""
        from datetime import date

        tournament = cls(
            name=data["name"],
            location=data["location"],
            start_date=date.fromisoformat(data["start_date"]),
            end_date=date.fromisoformat(data["end_date"]),
            number_of_rounds=data["number_of_rounds"],
            description=data["description"],
        )
        tournament.current_round = data["current_round"]
        tournament.players = [Player.from_dict(p) for p in data["players"]]
        tournament.rounds = [Round.from_dict(r) for r in data["rounds"]]
        return tournament
