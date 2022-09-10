from controller.database import save_database, load_tournament
from controller.player_controller import update_rankings
from controller.tournament_controller import create_tournament, play_tournament
from view.player_view import CreatePlayer
from view.report_view import Report
from view.tournament_view import LoadTournament
from view.view import CheckView


class MainMenu(CheckView):
    def display_main_menu(self):

        while True:

            print()
            user_input = self.get_user_entry(
                message_display="---Bienvenu que souhaitez-vous faire ?---\n\n"
                "1 - Créer un tournoi\n"
                "2 - Charger un tournoi\n"
                "3 - Créer des joueurs\n"
                "4 - Voir les rapports\n"
                "q - Quitter\n-> ",
                message_error="Veuillez entrer une valeur valide",
                value_type="selection",
                user_entry=["1", "2", "3", "4", "q"],
            )

            # Creer un tournoi
            if user_input == "1":
                tournament = create_tournament()
                break

            elif user_input == "2":
                serialized_tournament = LoadTournament().display_menu()

                if serialized_tournament:
                    tournament = load_tournament(serialized_tournament)
                    break

                else:
                    print("Il n'y a aucun tournoi présent dans la base")
                    continue

            elif user_input == "3":

                user_input = self.get_user_entry(
                    message_display="Nombre de joueurs créés : \n",
                    message_error="Veuillez indiquer une valeur numérique valide",
                    value_type="numeric",
                )
                for i in range(user_input):
                    serialized_new_player = CreatePlayer().display_menu()
                    save_database("players", serialized_new_player)

            elif user_input == "4":

                while True:
                    user_input = self.get_user_entry(
                        message_display="1 - Voir les joueurs \n2 - Voir les tournois\nr - Retour\n->",
                        message_error="Veuillez faire un choix valide.",
                        value_type="selection",
                        user_entry=["1", "2", "3", "r"],
                    )

                    if user_input == "r":
                        break

                    elif user_input == "1":

                        while True:
                            user_input = self.get_user_entry(
                                message_display="Consulter le classement des joueurs : \n"
                                "1 - Trier par rang \n"
                                "2 - Trier par ordre alphabétique\n"
                                "r - Retour\n->",
                                message_error="Veuillez faire un choix valide.",
                                value_type="selection",
                                user_entry=["1", "2", "r"],
                            )

                            if user_input == "r":
                                break

                            elif user_input == "1":
                                sorted_players = Report().sort_players(
                                    Report().players, by_rank=True
                                )
                                Report().display_players_report(players=sorted_players)

                            elif user_input == "2":
                                sorted_players = Report().sort_players(
                                    Report().players, by_rank=False
                                )
                                Report().display_players_report(players=sorted_players)

                    elif user_input == "2":

                        Report().display_tournaments_reports()
            else:
                quit()

        print()
        user_input = self.get_user_entry(
            message_display="---Que souhaitez-vous faire ?---\n\n"
            "1 - Jouer le tournoi\n"
            "q - Quitter \n->",
            message_error="Veuillez faire un choix valide",
            value_type="selection",
            user_entry=["1", "q"],
        )

        if user_input == "1":
            rankings = play_tournament(tournament, new_tournament_loaded=True)

        else:
            quit()

        print()
        print(
            f"Le tournois {tournament.name} est maintenant terminé. \nVoici les résultats : "
        )
        for i, player in enumerate(rankings):
            print(f"{str(i+1)} - {player}.")

        print()
        user_input = self.get_user_entry(
            message_display="Mis à jour des classements des joueurs \n"
            "1 - Mis à jour automatique\n"
            "2 - Mis à jour manuelle\n"
            "q - Quitter\n->",
            message_error="Veuillez faire un choix valide.",
            value_type="selection",
            user_entry=["1", "2", "q"],
        )

        if user_input == "1":
            for i, player in enumerate(rankings):
                print(player.name)
                update_rankings(player, i + 1)

        elif user_input == "2":
            for player in rankings:
                rank = self.get_user_entry(
                    message_display=f"Rang de {player} : \n\n",
                    message_error="Veuillez indiquer un nombre entier",
                    value_type="numeric",
                )
                update_rankings(player, rank)

        else:
            quit()
