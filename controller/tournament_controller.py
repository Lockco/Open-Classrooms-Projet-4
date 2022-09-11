from models.tournaments_models import Tournaments
from view.view import CheckView
from view.tournament_view import LoadTournament, CreateTournament
from view.player_view import LoadPlayer
from controller.player_controller import create_player, update_rankings
from controller.database import (
    save_database,
    load_player,
    update_database,
    load_tournament,
)


def create_tournament():

    menu = CheckView()
    user_entries = CreateTournament().display_tournament_menu()
    user_input = menu.get_user_entry(
        message_display="\n---Que souhaitez-vous faire ?---\n\n1 - Charger des joueurs\n2 - Créer des joueurs\n->",
        message_error="\nVeuillez faire un choix valide",
        value_type="selection",
        user_entry=["1", "2"],
    )

    if user_input == "1":
        players = []
        user_input = menu.get_user_entry(
            message_display="\nCombien de joueurs souhaitez-vous ajouter à la partie ?\n->",
            message_error="\nSaisissez un nombre entier.",
            value_type="numeric",
        )

        serialized_players = LoadPlayer().display_menu(nb_players_to_load=user_input)

        for serialized_player in serialized_players:
            player = load_player(serialized_player)
            players.append(player)

    else:

        print(f"Création de {str(user_entries['number_players'])} joueurs.")
        players = []
        while len(players) < user_entries["number_players"]:
            players.append(create_player())

    tournament = Tournaments(
        user_entries["name"],
        user_entries["place"],
        user_entries["date"],
        user_entries["time_control"],
        players,
        user_entries["number_of_rounds"],
        user_entries["description"],
    )
    # sauvegarde du tournois dans la base de donnée
    save_database("tournaments", tournament.get_serialized_tournament())

    return tournament


def play_tournament(tournament, new_tournament_loaded=False):
    menu = CheckView()
    print()
    print(f"Début du tournoi {tournament.name}\n")
    print()

    while True:

        # Dans le cas où un nouveau tournoi est chargé, on calcule le nombre de rounds restants à jouer
        a = 0
        if new_tournament_loaded:
            for round in tournament.rounds:
                if round.end_date == "":
                    a += 1
            nb_rounds_to_play = tournament.number_of_rounds - a
            new_tournament_loaded = False
        else:
            nb_rounds_to_play = tournament.number_of_rounds

        for i in range(nb_rounds_to_play):
            # On Créer le round
            tournament.create_round(round_number=i + a)

            # On joue le dernier round qui a été créé
            current_round = tournament.rounds[-1]
            print()
            print(current_round.start_date + " : Début du " + current_round.name)

            # Un fois le round terminé, on passe au round suivant
            # on peux aussi mettre à jour les classements manuellement
            while True:
                print()
                user_input = menu.get_user_entry(
                    message_display="---Que souhaitez-vous faire ?---\n\n"
                    "1 - Passer au round suivant\n"
                    "2 - Consulter les classements\n"
                    "3 - Mettre à jour les classements\n"
                    "4 - Sauvegarder le tournoi\n"
                    "5 - Charger un tournoi\n->",
                    message_error="Veuillez faire un choix valide",
                    value_type="selection",
                    user_entry=["1", "2", "3", "4", "5"],
                )
                print()

                # Pour passer au round suivant
                if user_input == "1":
                    current_round.next_round()
                    break

                # Pour Afficher les classements
                elif user_input == "2":
                    print(f"Classement du tournoi {tournament.name} : \n\n")
                    for i, player in enumerate(tournament.get_rankings()):
                        print(f"{str(i + 1)} - {player}")

                # Pour Mettre à jour les classements
                elif user_input == "3":
                    for player in tournament.players:
                        rank = menu.get_user_entry(
                            message_display=f"Mettez à jour le rang de {player} : \n->",
                            message_error="Veuillez saisir un nombre entier",
                            value_type="numeric",
                        )
                        update_rankings(player, rank, score=False)

                # Pour sauvegarder le tournoi
                elif user_input == "4":
                    rankings = tournament.get_rankings()
                    for i, player in enumerate(rankings):
                        for tour_player in tournament.players:
                            if player.name == tour_player.name:
                                tour_player.rank = str(i + 1)
                    update_database(
                        "tournaments",
                        tournament.get_serialized_tournament(save_rounds=True),
                    )

                # Pour charge un tournoi
                elif user_input == "5":
                    serialized_loaded_tournament = LoadTournament().display_menu()
                    tournament = load_tournament(serialized_loaded_tournament)
                    new_tournament_loaded = True
                    break

            if new_tournament_loaded:
                break

        if new_tournament_loaded:
            continue

        else:
            break

    # Lorsque le tournois est terminé, on le sauvegarde dans la
    # base de donnée et on retourne le résultat à l'utilisateur

    rankings = tournament.get_rankings()
    for i, player in enumerate(rankings):

        for tour_player in tournament.players:

            if player.name == tour_player.name:
                tour_player.total_score += player.tournament_score
                tour_player.rank = str(i + 1)

    update_database(
        "tournaments", tournament.get_serialized_tournament(save_rounds=True)
    )
    return rankings
