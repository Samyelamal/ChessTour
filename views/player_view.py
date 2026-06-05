"""Vues liées à l'affichage et à la saisie des joueurs."""

from datetime import date
import re


def display_all_players(players) -> None:
    """Affiche tous les joueurs enregistrés par ordre alphabétique."""
    print("\n=== JOUEURS ENREGISTRÉS ===")
    if not players:
        print("  Aucun joueur enregistré.")
        return

    for i, p in enumerate(
        sorted(players, key=lambda x: (x["last_name"], x["first_name"])), 1
    ):
        print(
            f"  {i}. "
            f"{p['last_name']} "
            f"{p['first_name']} "
            f"({p['national_id']})"
        )


def prompt_new_player() -> tuple:
    """Demande les informations du joueur avec validation champ par champ."""

    print("\n--- Nouveau joueur ---")

    while True:
        first_name = input("Prénom : ").strip()
        if first_name:
            break
        print("Le prénom ne peut pas être vide.")

    while True:
        last_name = input("Nom : ").strip()
        if last_name:
            break
        print("Le nom ne peut pas être vide.")

    while True:
        birth_date = input(
            "Date de naissance (AAAA-MM-JJ) : "
        ).strip()

        try:
            parsed_date = date.fromisoformat(birth_date)

            if parsed_date >= date.today():
                print("La date doit être dans le passé.")
                continue

            break

        except ValueError:
            print(
                "Format invalide. Exemple : 1990-05-12"
            )

    while True:
        national_id = input(
            "Identifiant national (ex: AB12345) : "
        ).strip().upper()

        if re.match(
            r"^[A-Z]{2}\d{5}$",
            national_id
        ):
            break

        print(
            "Format invalide. Exemple : AB12345"
        )

    return (
        first_name,
        last_name,
        birth_date,
        national_id,
    )