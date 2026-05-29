"""Utilitaires de sauvegarde et chargement des données en JSON."""

import json
from pathlib import Path

TOURNAMENTS_DIR = Path("data/tournaments")
PLAYERS_FILE = Path("data/players.json")


def _tournament_file(name: str) -> Path:
    """Retourne le chemin du fichier JSON d'un tournoi à partir de son nom."""
    safe_name = name.lower().replace(" ", "_")
    return TOURNAMENTS_DIR / f"{safe_name}.json"


def load_tournaments() -> list:
    """Charge et retourne la liste de tous les tournois depuis le dossier."""
    if not TOURNAMENTS_DIR.exists():
        return []
    tournaments = []
    for filepath in sorted(TOURNAMENTS_DIR.glob("*.json")):
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                tournaments.append(json.load(f))
            except json.JSONDecodeError:
                continue
    return tournaments


def save_tournament(tournament) -> None:
    """Sauvegarde un tournoi dans son propre fichier JSON."""
    TOURNAMENTS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = _tournament_file(tournament.name)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tournament.to_dict(), f, indent=4, ensure_ascii=False)


def load_players() -> list:
    """Charge et retourne la liste des joueurs depuis le fichier JSON."""
    if not PLAYERS_FILE.exists():
        return []
    with open(PLAYERS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_player(player) -> None:
    """Sauvegarde un nouveau joueur dans le fichier JSON si non existant."""
    PLAYERS_FILE.parent.mkdir(exist_ok=True)
    players = load_players()

    for p in players:
        if p["national_id"] == player.to_dict()["national_id"]:
            return

    players.append(player.to_dict())

    with open(PLAYERS_FILE, "w", encoding="utf-8") as f:
        json.dump(players, f, indent=4, ensure_ascii=False)
