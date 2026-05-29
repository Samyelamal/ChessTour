"""Point d'entrée de l'application de gestion de tournois d'échecs."""

from controllers.app_controller import AppController

if __name__ == "__main__":
    app = AppController()
    app.run()
