"""Contrôleur principal de l'application."""

from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from utils.json_manager import load_tournaments
from views.menu_view import display_main_menu, display_reports_menu
from views.tournament_view import (
    display_all_tournaments,
    display_tournament_details,
    display_tournament_players,
    display_tournament_rounds,
)


class AppController:
    """Gère la navigation entre les menus principaux de l'application."""

    def run(self) -> None:
        """Lance la boucle principale de l'application."""
        while True:
            display_main_menu()
            choice = input("Choix : ").strip()

            if choice == "1":
                TournamentController().create_tournament()
            elif choice == "2":
                TournamentController().load_tournament()
            elif choice == "3":
                PlayerController().run()
            elif choice == "4":
                self._reports()
            elif choice == "5":
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")

    def _reports(self) -> None:
        """Gère le sous-menu des rapports."""
        while True:
            display_reports_menu()
            choice = input("Choix : ").strip()

            if choice == "1":
                self._report_all_players()
            elif choice == "2":
                display_all_tournaments(load_tournaments())
            elif choice == "3":
                self._report_tournament_details()
            elif choice == "4":
                self._report_tournament_players()
            elif choice == "5":
                self._report_tournament_rounds()
            elif choice == "6":
                break
            else:
                print("Choix invalide.")

    def _report_all_players(self) -> None:
        """Affiche tous les joueurs connus, triés alphabétiquement."""
        from utils.json_manager import load_players
        from views.player_view import display_all_players
        display_all_players(load_players())

    def _pick_tournament(self):
        """Affiche la liste des tournois et retourne celui choisi par l'utilisateur."""
        tournaments = load_tournaments()
        display_all_tournaments(tournaments)
        if not tournaments:
            return None
        choice = input("\nNuméro du tournoi : ").strip().rstrip(".")
        if not choice.isdigit() or not (1 <= int(choice) <= len(tournaments)):
            print("Choix invalide.")
            return None
        return tournaments[int(choice) - 1]

    def _report_tournament_details(self) -> None:
        """Affiche les détails du tournoi sélectionné."""
        t = self._pick_tournament()
        if t:
            display_tournament_details(t)

    def _report_tournament_players(self) -> None:
        """Affiche les joueurs du tournoi sélectionné par ordre alphabétique."""
        t = self._pick_tournament()
        if t:
            display_tournament_players(t["players"])

    def _report_tournament_rounds(self) -> None:
        """Affiche les tours et matchs du tournoi sélectionné."""
        t = self._pick_tournament()
        if t:
            display_tournament_rounds(t["rounds"])
