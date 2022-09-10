from view.view import CheckView
from controller.database import load_database


class CreatePlayer(CheckView):
    def display_menu(self):

        name = input("---Indiquer le nom du joueur---\n")

        first_name = input("\n---Indiquer le prénom du joueur---\n")

        date_of_birth = self.get_user_entry(
            message_display="\nIndiquer la date de naissance (format DD-MM-AAAA):\n->",
            message_error="Veuillez entrer une date corespondant qu format indiqué (format DD-MM-AAAA) : \n",
            value_type="date",
        )

        gender = self.get_user_entry(
            message_display="\nIndiquer le sexe du joueur (H ou F):\n->",
            message_error="Veuillez entrer H ou F : ",
            value_type="selection",
            user_entry=["H", "h", "F", "f"],
        )

        ranking = self.get_user_entry(
            message_display="\nIndiquer le rang du joueur :\n->",
            message_error="Veuillez entrer une valeur numérique valide ",
            value_type="numeric",
        )

        print(f"\nLe joueur {first_name} {name} a bien été créé.\n")

        return {
            "name": name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "total_score": 0,
            "ranking": ranking,
        }


class LoadPlayer(CheckView):
    def display_menu(self, nb_players_to_load):

        all_players = load_database("players")
        serialized_loaded_players = []

        for i in range(nb_players_to_load):
            print(
                f"\nIl ne reste plus que {str(nb_players_to_load - i)} joueur(s) à charger."
            )
            display_message = "\nChoisissez un joueur\n"

            user_entry = []
            for i, player in enumerate(all_players):
                display_message = (
                    display_message
                    + f"{str(i+1)} - {player['first_name']} {player['name']}\n"
                )
                user_entry.append(str(i + 1))

            user_input = int(
                self.get_user_entry(
                    message_display=display_message,
                    message_error="Veuillez entrer un nombre entier ",
                    value_type="numeric",
                    user_entry=user_entry,
                )
            )

            if all_players[user_input - 1] not in serialized_loaded_players:
                serialized_loaded_players.append(all_players[user_input - 1])

            else:
                print(
                    "\nLe joueur a déjà été chargé, veuillez sélectionner un autre joueur.\n"
                )
                nb_players_to_load += 1

        return serialized_loaded_players
