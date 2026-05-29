"""Contrôleur gérant la création et le déroulement d'un tournoi."""

import random
from datetime import date

from models.match import Match
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from utils.json_manager import load_tournaments, save_tournament
from views.menu_view import display_tournament_menu
from views.tournament_view import (
    display_all_tournaments,
    display_players,
    display_round,
    prompt_match_result,
    prompt_new_player,
    prompt_new_tournament,
)


class TournamentController:
    """Gère la logique de création, chargement et déroulement d'un tournoi."""

    def __init__(self):
        """Initialise le contrôleur sans tournoi actif."""
        self.tournament = None

    def create_tournament(self) -> None:
        """Crée un nouveau tournoi à partir des saisies utilisateur."""
        name, location, start_date, end_date, number_of_rounds, description = (
            prompt_new_tournament()
        )
        try:
            self.tournament = Tournament(
                name=name,
                location=location,
                start_date=date.fromisoformat(start_date),
                end_date=date.fromisoformat(end_date),
                number_of_rounds=number_of_rounds,
                description=description,
            )
        except ValueError as e:
            print(f"Erreur : {e}")
            return
        save_tournament(self.tournament)
        print(f"\nTournoi « {name} » créé et sauvegardé.")
        self._manage_tournament()

    def load_tournament(self) -> None:
        """Charge un tournoi existant depuis le fichier JSON."""
        tournaments_data = load_tournaments()
        display_all_tournaments(tournaments_data)
        if not tournaments_data:
            return
        choice = input("\nNuméro du tournoi à charger : ").strip().rstrip(".")
        if not choice.isdigit() or not (1 <= int(choice) <= len(tournaments_data)):
            print("Choix invalide.")
            return
        self.tournament = Tournament.from_dict(tournaments_data[int(choice) - 1])
        print(f"\nTournoi « {self.tournament.name} » chargé.")
        self._manage_tournament()

    def _manage_tournament(self) -> None:
        """Boucle de gestion interactive d'un tournoi en cours."""
        while True:
            display_tournament_menu()
            choice = input("Choix : ").strip()

            if choice == "1":
                self._add_player()
            elif choice == "2":
                self._start_next_round()
            elif choice == "3":
                self._enter_results()
            elif choice == "4":
                display_players(self.tournament.players)
            elif choice == "5":
                break
            else:
                print("Choix invalide.")

    def _add_player(self) -> None:
        """Ajoute un joueur au tournoi après validation des données saisies."""
        first_name, last_name, birth_date, national_id = prompt_new_player()
        try:
            player = Player(
                first_name=first_name,
                last_name=last_name,
                birth_date=date.fromisoformat(birth_date),
                national_id=national_id,
            )
            self.tournament.add_player(player)
            save_tournament(self.tournament)
            print(f"{player.first_name} {player.last_name} ajouté(e).")
        except ValueError as e:
            print(f"Erreur : {e}")

    def _start_next_round(self) -> None:
        """Génère et lance le tour suivant si les conditions sont remplies."""
        t = self.tournament
        if t.current_round >= t.number_of_rounds:
            print("Tous les tours ont déjà été joués.")
            return
        if len(t.players) < 2:
            print("Il faut au moins 2 joueurs.")
            return
        if t.rounds and t.rounds[-1].end_time is None:
            print("Terminez le tour en cours avant d'en lancer un nouveau.")
            return

        round_ = Round(f"Round {t.current_round + 1}")
        for p1, p2 in self._generate_pairs():
            round_.add_match(Match(p1, p2))

        t.add_round(round_)
        save_tournament(t)
        display_round(round_)

    def _generate_pairs(self) -> list:
        """Génère les paires de joueurs selon le système suisse."""
        players = self.tournament.players[:]
        played = self._played_pairs()

        if self.tournament.current_round == 0:
            random.shuffle(players)
        else:
            players.sort(key=lambda p: p.score, reverse=True)

        pairs = []
        available = players[:]
        while len(available) >= 2:
            p1 = available.pop(0)
            for i, p2 in enumerate(available):
                if (p1.national_id, p2.national_id) not in played:
                    pairs.append((p1, p2))
                    available.pop(i)
                    break
            else:
                p2 = available.pop(0)
                pairs.append((p1, p2))
        return pairs

    def _played_pairs(self) -> set:
        """Retourne l'ensemble des paires de joueurs ayant déjà joué ensemble."""
        played = set()
        for round_ in self.tournament.rounds:
            for match in round_.matches:
                id1 = match.player_1.national_id
                id2 = match.player_2.national_id
                played.add((id1, id2))
                played.add((id2, id1))
        return played

    def _enter_results(self) -> None:
        """Saisit les résultats des matchs du tour en cours."""
        t = self.tournament
        if not t.rounds:
            print("Aucun tour en cours. Lancez d'abord un tour.")
            return
        current = t.rounds[-1]
        if current.end_time is not None:
            print("Ce tour est déjà terminé.")
            return
        for i, match in enumerate(current.matches, 1):
            if match.score_1 is not None:
                continue
            score_1, score_2 = prompt_match_result(match, i)
            match.set_result(score_1, score_2)

        current.close_round()
        save_tournament(t)
        print("\nRésultats enregistrés.")
        display_players(t.players)
