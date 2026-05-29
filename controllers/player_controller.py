"""Contrôleur gérant la gestion des joueurs."""

from datetime import date

from models.player import Player
from utils.json_manager import load_players, save_player
from views.menu_view import display_players_menu
from views.player_view import display_all_players, prompt_new_player


class PlayerController:
    """Gère l'ajout et la consultation des joueurs."""

    def run(self) -> None:
        """Boucle du menu de gestion des joueurs."""
        while True:
            display_players_menu()
            choice = input("Choix : ").strip()

            if choice == "1":
                self._add_player()
            elif choice == "2":
                display_all_players(load_players())
            elif choice == "3":
                break
            else:
                print("Choix invalide.")

    def _add_player(self) -> None:
        """Crée un joueur et le sauvegarde dans la base de joueurs."""
        first_name, last_name, birth_date, national_id = prompt_new_player()
        try:
            player = Player(
                first_name=first_name,
                last_name=last_name,
                birth_date=date.fromisoformat(birth_date),
                national_id=national_id,
            )
            save_player(player)
            print(f"{player.first_name} {player.last_name} enregistré(e).")
        except ValueError as e:
            print(f"Erreur : {e}")
