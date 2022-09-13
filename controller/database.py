from pathlib import Path
from tinydb import TinyDB
from tinydb import where
from models.player_models import Player
from models.tournaments_models import Tournaments
from models.round__models import Round
from models.match_models import Match


def save_database(database_name, serialized_data):
    """Fonction de sauvegarde de la base"""
    Path("data/").mkdir(exist_ok=True)
    try:
        db = TinyDB(f"data/{database_name}.json", indent=4)

    except FileNotFoundError:
        with open(f"data{database_name}.json", "w"):
            pass

        db = TinyDB("data/" + {database_name} + ".json")

    db.insert(serialized_data)
    print(f"{serialized_data['name']} sauvegardé avec succès.")


def update_database(database_name, serialized_data):
    """Fonction de mis à jour des donnée"""

    db = TinyDB(f"data/{database_name}.json")
    db.update(serialized_data, where("name") == serialized_data["name"])
    print(f"{serialized_data['name']} mis à jour avec succès.")


def update_player_rank(database_name, serialized_data):
    """Fonction de mis à jour du rang du joueur"""

    db = TinyDB(f"data/{database_name}.json")
    db.update(
        {
            "ranking": serialized_data["ranking"],
            "total_score": serialized_data["total_score"],
        },
        where("name") == serialized_data["name"],
    )
    print(f"{serialized_data['name']} mis à jour avec succès")


def load_database(database_name):
    """Fonction de chargement de la base de donnée"""

    db = TinyDB(f"data/{database_name}.json")
    return db.all()


def load_player(serialized_player, load_tournament_score=False):
    """Fonction de chargement des joueurs"""

    player = Player(
        serialized_player["name"],
        serialized_player["first_name"],
        serialized_player["date_of_birth"],
        serialized_player["gender"],
        serialized_player["total_score"],
        serialized_player["ranking"],
    )

    if load_tournament_score:

        player.tournament_score = serialized_player["tournament_score"]

    return player


def load_tournament(serialized_tournament):
    """Fonction de chargement des tournois"""

    loaded_tournament = Tournaments(
        serialized_tournament["name"],
        serialized_tournament["place"],
        serialized_tournament["date"],
        serialized_tournament["time_control"],
        [
            load_player(player, load_tournament_score=True)
            for player in serialized_tournament["players"]
        ],
        serialized_tournament["number_of_rounds"],
        serialized_tournament["description"],
    )

    loaded_tournament.rounds = load_rounds(serialized_tournament, loaded_tournament)

    return loaded_tournament


def load_rounds(serialized_tournament, tournament):
    """Fonction de chargement des rounds"""

    loaded_rounds = []

    for round in serialized_tournament["rounds"]:
        print(f"***Liste des rounds  = {round}\n\n***")
        pair_p1 = None
        pair_p2 = None
        players_pairs = []
        for pair in round["players_pairs"]:
            for player in tournament.players:
                print(f"***\nInfo joueurs : {player}\n***\n")
                if player.name == pair[0]["first_name"]:
                    pair_p1 = player
                elif player.name == pair[1]["first_name"]:
                    pair_p2 = player
            players_pairs.append((pair_p1, pair_p2))

        loaded_round = Round(round["name"], players_pairs, load_match=True)

        loaded_round.matchs = [
            load_match(match, tournament) for match in round["matchs"]
        ]
        loaded_round.start_date = round["start_date"]
        loaded_round.end_date = round["end_date"]
        loaded_rounds.append(loaded_round)

        return loaded_rounds


def load_match(serialized_match, tournament):
    """Fonction de chargement des matchs"""
    player1 = None
    player2 = None
    for player in tournament.players:
        if player.name == serialized_match["player1"]["first_name"]:
            player1 = player
        elif player.name == serialized_match["player2"]["first_name"]:
            player2 = player

    loaded_match = Match(players_pair=(player1, player2), name=serialized_match["name"])

    loaded_match.score_player1 = serialized_match["score_player1"]
    loaded_match.color_player1 = serialized_match["color_player1"]
    loaded_match.score_player2 = serialized_match["score_player2"]
    loaded_match.color_player2 = serialized_match["color_player2"]
    loaded_match.winner = serialized_match["winner"]

    return loaded_match
