"""Modèle représentant un tour dans un tournoi d'échecs."""

from datetime import datetime

from models.match import Match


class Round:
    """Représente un tour contenant une liste de matchs."""

    def __init__(self, name: str):
        """Initialise un tour avec son nom et l'heure de début."""
        self.name = name
        self.matches = []
        self.start_time = datetime.now()
        self.end_time = None

    def add_match(self, match) -> None:
        """Ajoute un match au tour."""
        self.matches.append(match)

    def close_round(self) -> None:
        """Marque le tour comme terminé en enregistrant l'heure de fin."""
        self.end_time = datetime.now()

    def to_dict(self) -> dict:
        """Sérialise le tour en dictionnaire."""
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Round":
        """Crée un tour à partir d'un dictionnaire."""
        round_ = cls(data["name"])
        round_.matches = [Match.from_dict(m) for m in data["matches"]]
        round_.start_time = datetime.fromisoformat(data["start_time"])
        if data["end_time"]:
            round_.end_time = datetime.fromisoformat(data["end_time"])
        return round_
