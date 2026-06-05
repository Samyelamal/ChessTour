"""Vues liées à l'affichage et à la saisie des données de tournoi."""

from datetime import date


def display_players(players) -> None:
    """Affiche le classement des joueurs trié par score décroissant."""
    print("\n=== CLASSEMENT ===")
    for player in sorted(players, key=lambda p: p.score, reverse=True):
        print(f"{player.first_name} {player.last_name} : {player.score}")


def display_round(round_) -> None:
    """Affiche les matchs d'un tour."""
    print(f"\n=== {round_.name} ===")
    for i, match in enumerate(round_.matches, 1):
        p1 = match.player_1
        p2 = match.player_2
        print(
            f"  Match {i} : "
            f"{p1.first_name} {p1.last_name} vs "
            f"{p2.first_name} {p2.last_name}"
        )


def display_all_tournaments(tournaments) -> None:
    """Affiche la liste de tous les tournois enregistrés."""
    print("\n=== TOURNOIS ===")

    if not tournaments:
        print("  Aucun tournoi enregistré.")
        return

    for i, t in enumerate(tournaments, 1):
        print(
            f"  {i}. "
            f"{t['name']} — "
            f"{t['start_date']} / "
            f"{t['end_date']}"
        )

    print("  (Entrez le numéro du tournoi)")


def display_tournament_details(tournament) -> None:
    """Affiche les détails d'un tournoi."""
    print(f"\n=== {tournament['name']} ===")
    print(f"  Lieu       : {tournament['location']}")
    print(f"  Début      : {tournament['start_date']}")
    print(f"  Fin        : {tournament['end_date']}")
    print(f"  Tours      : {tournament['number_of_rounds']}")
    print(f"  Description: {tournament['description']}")


def display_tournament_players(players) -> None:
    """Affiche les joueurs d'un tournoi par ordre alphabétique."""
    print("\n=== JOUEURS DU TOURNOI ===")

    for p in sorted(
        players,
        key=lambda x: (x["last_name"], x["first_name"])
    ):
        print(
            f"  {p['last_name']} "
            f"{p['first_name']} "
            f"({p['national_id']})"
        )


def display_tournament_rounds(rounds) -> None:
    """Affiche tous les tours et matchs d'un tournoi."""
    print("\n=== TOURS ET MATCHS ===")

    for round_ in rounds:
        print(f"\n  {round_['name']}")

        for i, match in enumerate(round_["matches"], 1):
            p1 = match["player_1"]
            p2 = match["player_2"]

            print(
                f"    Match {i} : "
                f"{p1['first_name']} "
                f"{p1['last_name']} "
                f"({match['score_1']}) vs "
                f"{p2['first_name']} "
                f"{p2['last_name']} "
                f"({match['score_2']})"
            )


def prompt_new_tournament() -> tuple:
    """Demande les informations pour créer un tournoi."""

    print("\n=== NOUVEAU TOURNOI ===")

    while True:
        name = input("Nom du tournoi : ").strip()

        if name:
            break

        print("Le nom du tournoi ne peut pas être vide.")

    while True:
        location = input("Lieu : ").strip()

        if location:
            break

        print("Le lieu ne peut pas être vide.")

    while True:
        start_date = input(
            "Date de début (AAAA-MM-JJ) : "
        ).strip()

        try:
            date.fromisoformat(start_date)
            break

        except ValueError:
            print(
                "Format invalide. Exemple : 2025-01-15"
            )

    while True:
        end_date = input(
            "Date de fin (AAAA-MM-JJ) : "
        ).strip()

        try:
            date.fromisoformat(end_date)
            break

        except ValueError:
            print(
                "Format invalide. Exemple : 2025-01-20"
            )

    while True:
        rounds_input = input(
            "Nombre de tours (défaut 4) : "
        ).strip()

        if not rounds_input:
            number_of_rounds = 4
            break

        if rounds_input.isdigit():
            number_of_rounds = int(rounds_input)
            break

        print("Veuillez entrer un nombre valide.")

    description = input("Description : ").strip()

    return (
        name,
        location,
        start_date,
        end_date,
        number_of_rounds,
        description,
    )


def prompt_new_player() -> tuple:
    """Demande les informations pour ajouter un joueur."""
    print("\n--- Ajouter un joueur ---")

    first_name = input("Prénom : ").strip()
    last_name = input("Nom : ").strip()
    birth_date = input(
        "Date de naissance (AAAA-MM-JJ) : "
    ).strip()
    national_id = input(
        "Identifiant national (ex: AB12345) : "
    ).strip()

    return (
        first_name,
        last_name,
        birth_date,
        national_id,
    )


def prompt_match_result(match, index: int) -> tuple:
    """Demande le résultat d'un match."""

    p1 = match.player_1
    p2 = match.player_2

    print(
        f"\n  Match {index} : "
        f"{p1.first_name} {p1.last_name} "
        f"vs "
        f"{p2.first_name} {p2.last_name}"
    )

    while True:
        print("    1. Victoire joueur 1")
        print("    2. Victoire joueur 2")
        print("    3. Match nul")

        choice = input(
            "    Résultat : "
        ).strip()

        if choice == "1":
            return 1, 0

        if choice == "2":
            return 0, 1

        if choice == "3":
            return 0.5, 0.5

        print("Choix invalide.")