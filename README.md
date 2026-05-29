# Chess Tournament Manager

Application Python de gestion de tournois d'échecs en console, fonctionnant entièrement hors ligne.

## Fonctionnalités

- Créer et gérer des tournois d'échecs
- Ajouter des joueurs avec leur identifiant national
- Générer les appariements automatiquement (système suisse)
- Saisir les résultats des matchs tour par tour
- Consulter le classement en temps réel
- Sauvegarder et charger les tournois (fichiers JSON)
- Afficher des rapports : joueurs, tournois, tours et matchs

## Prérequis

- Python 3.10 ou supérieur
- pip

## Installation

Cloner le dépôt :

```bash
git clone <url-du-repo>
cd "Projet 4"
```

Créer et activer un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Lancer le programme

```bash
python3 main.py
```

## Structure du projet

Projet 4/
├── controllers/
│   ├── app_controller.py        # Contrôleur principal
│   └── tournament_controller.py # Contrôleur de tournoi
├── models/
│   ├── match.py                 # Modèle Match
│   ├── player.py                # Modèle Joueur
│   ├── round.py                 # Modèle Tour
│   └── tournament.py            # Modèle Tournoi
├── views/
│   ├── menu_view.py             # Affichage des menus
│   └── tournament_view.py       # Affichage et saisie tournoi
├── utils/
│   └── json_manager.py          # Sauvegarde/chargement JSON
├── data/
│   └── tournaments.json         # Données des tournois
├── flake8_rapport/              # Rapport de conformité PEP 8
├── main.py                      # Point d'entrée
├── requirements.txt
└── README.md

## Utilisation

1. Lancer le programme avec `python3 main.py`
2. Choisir **Nouveau tournoi** pour créer un tournoi
3. Ajouter au moins 2 joueurs (identifiant national : 2 lettres + 5 chiffres, ex: `AB12345`)
4. Lancer le **tour suivant** pour générer les appariements
5. Saisir les **résultats** de chaque match
6. Répéter jusqu'à la fin du tournoi
7. Consulter les **rapports** depuis le menu principal

## Générer un nouveau rapport flake8

```bash
flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport controllers models utils views main.py
```

Le rapport est généré dans le dossier `flake8_rapport/` et peut être ouvert avec `flake8_rapport/index.html`.