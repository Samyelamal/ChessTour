"""Utilitaires de sauvegarde et chargement des tournois en JSON."""

import json
from pathlib import Path

DATA_FILE = Path("data/tournaments.json")


def load_tournaments() -> list:
    """Charge et retourne la liste des tournois depuis le fichier JSON."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tournament(tournament) -> None:
    """Sauvegarde ou met à jour un tournoi dans le fichier JSON."""
    DATA_FILE.parent.mkdir(exist_ok=True)
    tournaments = load_tournaments()
    tournament_dict = tournament.to_dict()

    for i, t in enumerate(tournaments):
        if t["name"] == tournament_dict["name"]:
            tournaments[i] = tournament_dict
            break
    else:
        tournaments.append(tournament_dict)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tournaments, f, indent=4, ensure_ascii=False)
