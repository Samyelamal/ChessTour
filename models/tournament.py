class Tournament:
    """
    Modèle représentant un tournoi d'échecs.
    """

    def __init__(
        self,
        name: str,
        location: str,
        start_date,
        end_date,
        number_of_rounds: int = 4,
        description: str = "",
    ):
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
        self.players.append(player)

    def add_round(self, round_) -> None:
        self.rounds.append(round_)
        self.current_round += 1
