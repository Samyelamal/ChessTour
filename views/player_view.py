"""Vues liées à l'affichage et à la saisie des joueurs."""


def display_all_players(players) -> None:
    """Affiche tous les joueurs enregistrés par ordre alphabétique."""
    print("\n=== JOUEURS ENREGISTRÉS ===")
    if not players:
        print("  Aucun joueur enregistré.")
        return
    for i, p in enumerate(
        sorted(players, key=lambda x: (x["last_name"], x["first_name"])), 1
    ):
        print(f"  {i}. {p['last_name']} {p['first_name']} ({p['national_id']})")


def prompt_new_player() -> tuple:
    """Demande à l'utilisateur les informations pour créer un joueur."""
    print("\n--- Nouveau joueur ---")
    first_name = input("Prénom : ").strip()
    last_name = input("Nom : ").strip()
    birth_date = input("Date de naissance (AAAA-MM-JJ) : ").strip()
    national_id = input("Identifiant national (ex: AB12345) : ").strip()
    return first_name, last_name, birth_date, national_id
