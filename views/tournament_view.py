def display_players(players):

    print("\n=== CLASSEMENT ===")

    for player in players:
        print(
            f"{player.first_name} "
            f"{player.last_name} : "
            f"{player.score}"
        )
