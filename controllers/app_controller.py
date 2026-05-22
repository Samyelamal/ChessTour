from views.menu_view import display_main_menu
from controllers.tournament_controller import TournamentController


class AppController:

    def run(self):

        while True:

            display_main_menu()

            choice = input("Choix : ")

            if choice == "1":
                controller = TournamentController()
                controller.run_simulation()

            elif choice == "2":
                print("Au revoir")
                break

            else:
                print("Choix invalide")
