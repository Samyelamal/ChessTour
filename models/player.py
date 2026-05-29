"""Modèle représentant un joueur d'échecs."""

import re
from datetime import date


class Player:
    """Représente un joueur avec ses informations personnelles et son score."""

    NATIONAL_ID_REGEX = r"^[A-Z]{2}\d{5}$"

    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_date: date,
        national_id: str,
    ):
        """Initialise un joueur et valide ses données."""
        self.first_name = self._clean_name(first_name)
        self.last_name = self._clean_name(last_name)
        self.birth_date = self._validate_birth_date(birth_date)
        self.national_id = self._validate_national_id(national_id)
        self.score = 0.0

    @staticmethod
    def _clean_name(value: str) -> str:
        """Nettoie et valide un nom ou prénom."""
        if not value or not value.strip():
            raise ValueError("Le nom/prénom ne peut pas être vide.")
        return value.strip().title()

    @staticmethod
    def _validate_birth_date(value: date) -> date:
        """Vérifie que la date de naissance est dans le passé."""
        if value >= date.today():
            raise ValueError("La date de naissance doit être dans le passé.")
        return value

    @classmethod
    def _validate_national_id(cls, value: str) -> str:
        """Vérifie le format de l'identifiant national (ex: AB12345)."""
        if not re.match(cls.NATIONAL_ID_REGEX, value):
            raise ValueError("Identifiant national invalide (ex: AB12345).")
        return value

    def add_score(self, points: float) -> None:
        """Ajoute des points au score du joueur."""
        self.score += points

    def to_dict(self) -> dict:
        """Sérialise le joueur en dictionnaire."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat(),
            "national_id": self.national_id,
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        """Crée un joueur à partir d'un dictionnaire."""
        player = cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=date.fromisoformat(data["birth_date"]),
            national_id=data["national_id"],
        )
        player.score = data["score"]
        return player
