"""Vues du menu principal et des sous-menus."""


def display_main_menu() -> None:
    """Affiche le menu principal."""
    print("\n=== MENU PRINCIPAL ===")
    print("1. Nouveau tournoi")
    print("2. Charger un tournoi")
    print("3. Rapports")
    print("4. Quitter")


def display_tournament_menu() -> None:
    """Affiche le menu de gestion d'un tournoi."""
    print("\n=== GESTION DU TOURNOI ===")
    print("1. Ajouter un joueur")
    print("2. Lancer le tour suivant")
    print("3. Saisir les résultats du tour en cours")
    print("4. Voir le classement")
    print("5. Retour au menu principal")


def display_reports_menu() -> None:
    """Affiche le menu des rapports."""
    print("\n=== RAPPORTS ===")
    print("1. Liste de tous les joueurs (alphabétique)")
    print("2. Liste de tous les tournois")
    print("3. Détails d'un tournoi")
    print("4. Joueurs d'un tournoi (alphabétique)")
    print("5. Tours et matchs d'un tournoi")
    print("6. Retour")
