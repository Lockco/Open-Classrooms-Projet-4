from controller.database import load_database
from controller.timestamp_controller import timestamp
from view.view import CheckView


class CreateTournament(CheckView):
    def display_tournament_menu(self):

        date = timestamp()
        print("Un nouveau tournoi a été créé à la date du " + date)

        name = input("\nSaissisez le nom du tournoi : \n->")

        place = self.get_user_entry(
            message_display="\nOù a lieu du tournoi\n->",
            message_error="Veuillez entrer un lieu valide",
            value_type="string",
        )

        user_selection_time_control = self.get_user_entry(
            message_display="\nContrôle de temps:\n0 - Bullet\n1 - Blitz\n2 - Coup Rapide\n->",
            message_error="Veuillez entrer 0, 1 ou 2.",
            value_type="selection",
            user_entry=["0", "1", "2"],
        )

        if user_selection_time_control == "0":
            time_control = "Bullet"
        elif user_selection_time_control == "1":
            time_control = "Blitz"
        else:
            time_control = "Coup Rapide"

        number_players = self.get_user_entry(
            message_display="\nIndiquer le nombre de joueurs: \n->",
            message_error="Veuillez entrer un nombre entier supérieur ou égal à 2.",
            value_type="number_superior",
            default_value=2,
        )

        number_of_rounds = self.get_user_entry(
            message_display="\nIndiquer le nombre de tours (4 par défaut) : \n->",
            message_error="Veuillez entrer 4 ou plus.",
            value_type="number_superior",
            default_value=4,
        )
        description = input("\nDescription du tournoi : \n->")

        return {
            "name": name,
            "place": place,
            "date": date,
            "time_control": time_control,
            "number_players": number_players,
            "number_of_rounds": number_of_rounds,
            "description": description,
        }


class LoadTournament(CheckView):
    def display_menu(self):

        all_tournaments = load_database("tournaments")
        if all_tournaments:

            builded_selection = self.build_selection(
                iterable=all_tournaments,
                display_message=("Choisir un tournoi: \n"),
                user_entry=[],
            )

            user_input = int(
                self.get_user_entry(
                    message_display=builded_selection["message"] + "\n-> ",
                    message_error="Veuillez entrer un nombre entier.",
                    value_type="selection",
                    user_entry=builded_selection["user_entry"],
                )
            )
            serialized_loaded_tournament = all_tournaments[user_input - 1]

            return serialized_loaded_tournament

        else:
            return False
