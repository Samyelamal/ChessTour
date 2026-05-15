from datetime import date
import random

from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament


# Création des joueurs
players = [
    Player("Alice", "Dupont", date(1990, 5, 12), "AB12345"),
    Player("Bob", "Martin", date(1988, 3, 4), "CD23456"),
    Player("Claire", "Durand", date(1995, 7, 22), "EF34567"),
    Player("David", "Petit", date(1992, 11, 9), "GH45678"),
]

# Création du tournoi
tournament = Tournament(
    "Tournoi Test",
    "Paris",
    date.today(),
    date.today(),
    description="Simulation étape 1"
)

for player in players:
    tournament.add_player(player)

# Création d’un tour
round_1 = Round("Round 1")

match_1 = Match(players[0], players[1])
match_2 = Match(players[2], players[3])

match_1.set_result(*random.choice([(1, 0), (0, 1), (0.5, 0.5)]))
match_2.set_result(*random.choice([(1, 0), (0, 1), (0.5, 0.5)]))

round_1.add_match(match_1)
round_1.add_match(match_2)
round_1.close_round()

tournament.add_round(round_1)

# Vérification
for player in tournament.players:
    print(player.first_name, player.last_name, player.score)