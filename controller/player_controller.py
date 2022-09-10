from models.player_models import Player
from controller.database import save_database, update_player_rank
from view.player_view import CreatePlayer

"""fichier responsable de la gestion des fonctionnalitées lié à la création des joueurs"""


def create_player():
    user_entries = CreatePlayer().display_menu()

    player = Player(
        user_entries["first_name"],
        user_entries["name"],
        user_entries["date_of_birth"],
        user_entries["gender"],
        user_entries["total_score"],
        user_entries["ranking"],
    )

    # serialization:
    serialized_player = player.get_serialized_player()
    print(serialized_player)

    save_database("players", serialized_player)

    return player


def update_rankings(player, rank, score=True):
    if score:
        player.total_score += player.tournament_score
    player.rank = rank
    serialized_player = player.get_serialized_player(save_tournament_score=True)
    update_player_rank("players", serialized_player)
    print(
        f"Mis à jour du rang de {player}:\nScore total: {player.total_score}\nRang: {player.rank}"
    )
