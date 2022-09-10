from view.view import CheckView
from operator import itemgetter
from controller.database import load_database


class Report(CheckView):
    def __init__(self):

        self.players = load_database("players")
        self.tournament = load_database("tournaments")

    def display_players_report(self, players=[]):

        players = players

        builded_selection = self.build_selection(
            iterable=players,
            display_message="Consulter les détails du joueur : \n\n",
            user_entry=["r"],
        )

        while True:

            print("Classement : \n\n")

            user_input = self.get_user_entry(
                message_display=builded_selection["message"] + "r - Retour\n\n->",
                message_error="Votre choix est invalide",
                value_type="selection",
                user_entry=builded_selection["user_entry"],
            )

            if user_input == "r":
                break

            else:
                selected_player = players[int(user_input) - 1]

                while True:

                    print(f"Détails du joueur {selected_player['name']} : \n")
                    print(
                        f"Rang: {selected_player['ranking']}\n"
                        f"Score total: {selected_player['total_score']}\n"
                        f"Nom: {selected_player['name']}\n"
                        f"Prénom: {selected_player['first_name']}\n"
                        f"Date de naissance: {selected_player['date_of_birth']}\n"
                        f"Sexe: {selected_player['gender']}\n"
                    )
                    user_input = self.get_user_entry(
                        message_display="---Que souhaitez-vous faire ?--- \n\nr- Retour\n\n->",
                        message_error="Veuillez faire un choix valide.",
                        value_type="selection",
                        user_entry=["r"],
                    )

                    if user_input == "r":
                        break

    def display_tournaments_reports(self):

        builded_selection = self.build_selection(
            iterable=self.tournament,
            display_message="Consulter les détails d un tournoi : \n\n",
            user_entry=["r"],
        )

        while True:
            print("Tournois : ")

            user_input = self.get_user_entry(
                message_display=builded_selection["message"] + "r - Retour\n\n->",
                message_error="Veuillez faire un choix valide.",
                value_type="selection",
                user_entry=builded_selection["user_entry"],
            )

            if user_input == "r":
                break

            else:
                selected_tournament = self.tournament[int(user_input) - 1]

                while True:

                    print(
                        f"Détails du tournoi {selected_tournament['name']}\n"
                        f"Nom: {selected_tournament['name']}\n"
                        f"Lieu: {selected_tournament['place']}\n"
                        f"Date: {selected_tournament['date']}\n"
                        f"Contrôle du temps: {selected_tournament['time_control']}\n"
                        f"Nombre de rounds: {selected_tournament['number_of_rounds']}\n"
                        f"Description: {selected_tournament['description']}\n"
                    )

                    user_input = self.get_user_entry(
                        message_display="---Que souhaitez-vous faire ?---\n\n"
                        "1 - Voir les participants\n"
                        "2 - Voir les tours\n"
                        "r - Retour\n"
                        "->",
                        message_error="Veuillez entrer une sélection valide",
                        value_type="selection",
                        user_entry=["1", "2", "3", "r"],
                    )

                    if user_input == "r":
                        break

                    elif user_input == "1":

                        while True:
                            user_input = self.get_user_entry(
                                message_display="Type de classement :\n\n"
                                "1 - Trier par rang\n"
                                "2 - Trier par ordre alphabétique\n"
                                "r - Retour\n"
                                "->",
                                message_error=" Veuillez entrer une sélection valide",
                                value_type="selection",
                                user_entry=["1", "2", "r"],
                            )

                            if user_input == "r":
                                break

                            elif user_input == "1":
                                sorted_players = self.sort_players(
                                    selected_tournament["players"], by_rank=True
                                )
                                self.display_players_report(players=sorted_players)

                            elif user_input == "2":
                                sorted_players = self.sort_players(
                                    selected_tournament["players"], by_rank=False
                                )
                                self.display_players_report(players=sorted_players)

                    elif user_input == "2":
                        self.display_rounds(selected_tournament["rounds"])

    def display_rounds(self, rounds: list):
        builded_selection = self.build_selection(
            iterable=rounds,
            display_message="Consulter les détails d un round:\n\n",
            user_entry=["r"],
        )

        while True:

            print("Rounds : ")

            user_input = self.get_user_entry(
                message_display=builded_selection["message"] + "r- Retour\n",
                message_error="Veuillez faire un choix valide.",
                value_type="selection",
                user_entry=builded_selection["user_entry"],
            )

            if user_input == "r":
                break

            else:
                selected_round = rounds[int(user_input) - 1]
                while True:
                    print(
                        f"Détails du round {selected_round['name']}\n"
                        f"Nom: {selected_round['name']}\n"
                        f"Nombre de matchs: {len(selected_round['matchs'])}\n"
                        f"Date de début: {selected_round['start_date']}\n"
                        f"Date de fin: {selected_round['end_date']}\n"
                    )
                    user_input = self.get_user_entry(
                        message_display="---Que souhaitez-vous faire ?---\n\n1 - Voir les matchs\nr - Retour\n->",
                        message_error="Veuillez faire un choix valide",
                        value_type="selection",
                        user_entry=["1", "r"],
                    )

                    if user_input == "r":
                        break

                    else:
                        builded_selection = self.build_selection(
                            iterable=selected_round["matchs"],
                            display_message="Voir les détails d un match\n\n",
                            user_entry=["r"],
                        )

                        print("Matchs : ")
                        user_input = self.get_user_entry(
                            message_display=builded_selection["message"]
                            + "r - Retour\n\n->",
                            message_error="Veuillez faire un choix valide.",
                            value_type="selection",
                            user_entry=builded_selection["user_entry"],
                        )

                        if user_input == "r":
                            break

                        else:
                            selected_match = selected_round["matchs"][
                                int(user_input) - 1
                            ]

                            while True:
                                print(
                                    f"Consulter les détails du {selected_match['name']}\n\n"
                                    f"Joueur n°1 ({selected_match['color_player1']}):"
                                    + f"{selected_match['player1']['name']}"
                                    + f"({selected_match['score_player1']} points)\n"
                                    f"Joueur n°2 ({selected_match['color_player2']}): "
                                    + f"{selected_match['player2']['name']}"
                                    + f"({selected_match['score_player2']} points)\n"
                                    f"Gagnant : {selected_match['winner']}\n"
                                )

                                user_input = self.get_user_entry(
                                    message_display="---Que souhaitez-vous faire ?---\n\nr- Retour\n\n->",
                                    message_error="Veuillez faire un choix valide",
                                    value_type="selection",
                                    user_entry=["r"],
                                )

                                if user_input == "r":
                                    break

    @staticmethod
    def sort_players(players: list, by_rank: bool) -> list:

        if by_rank:
            sorted_players = sorted(players, key=itemgetter("ranking"))
        else:
            sorted_players = sorted(players, key=itemgetter("name"))

        return sorted_players
