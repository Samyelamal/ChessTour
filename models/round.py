from datetime import datetime


class Round:
    """
    Modèle représentant un tour du tournoi.
    """

    def __init__(self, name: str):
        self.name = name
        self.matches = []
        self.start_time = datetime.now()
        self.end_time = None

    def add_match(self, match) -> None:
        self.matches.append(match)

    def close_round(self) -> None:
        self.end_time = datetime.now()
