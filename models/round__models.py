from models.match_models import Match
from controller.timestamp_controller import timestamp


class Round:
    def __init__(self, name, players_pairs, load_match: bool = False):

        self.name = name
        self.players_pairs = players_pairs

        # Si on charge une partie, on assigne une liste vide aux matchs de manière a les charger.
        # Sinon, ont les créer normalement

        if load_match:
            self.matchs = []
        else:
            self.matchs = self.create_matchs()

        self.start_date = timestamp()
        self.end_date = ""

    def __str__(self):
        return self.name

    def create_matchs(self):
        """Création du match"""
        matchs = []
        for i, pair in enumerate(self.players_pairs):
            matchs.append(Match(name=f"Match {i}", players_pair=pair))

        return matchs

    def next_round(self):
        """fonction de génération du round suivant"""
        self.end_date = timestamp()
        print(f"{self.end_date} : {self.name} terminé.")
        print("Rentrer les résultats des matchs : ")

        for match in self.matchs:
            match.play_match()

    def get_serialized_round(self):
        print(self.players_pairs)
        ser_players_pairs = []
        for pair in self.players_pairs:
            ser_players_pairs.append(
                (
                    pair[0].get_serialized_player(save_tournament_score=True),
                    pair[1].get_serialized_player(save_tournament_score=True),
                )
            )

        return {
            "name": self.name,
            "players_pairs": ser_players_pairs,
            "matchs": [match.get_serialized_match() for match in self.matchs],
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
