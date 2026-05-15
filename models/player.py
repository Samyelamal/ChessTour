from datetime import date
import re


class Player:
    """
    Modèle représentant un joueur d'échecs.
    """

    NATIONAL_ID_REGEX = r"^[A-Z]{2}\d{5}$"

    def __init__(self, first_name: str, last_name: str, birth_date: date, national_id: str):
        self.first_name = self._clean_name(first_name)
        self.last_name = self._clean_name(last_name)
        self.birth_date = self._validate_birth_date(birth_date)
        self.national_id = self._validate_national_id(national_id)
        self.score = 0.0

    @staticmethod
    def _clean_name(value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Le nom/prénom ne peut pas être vide.")
        return value.strip().title()

    @staticmethod
    def _validate_birth_date(value: date) -> date:
        if value >= date.today():
            raise ValueError("La date de naissance doit être dans le passé.")
        return value

    @classmethod
    def _validate_national_id(cls, value: str) -> str:
        if not re.match(cls.NATIONAL_ID_REGEX, value):
            raise ValueError("Identifiant national invalide (ex: AB12345).")
        return value

    def add_score(self, points: float) -> None:
        self.score += points
