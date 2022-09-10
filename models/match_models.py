import random
from view.view import CheckView


class Match:

    """dans l"init on préciser le nom du joueur, son score, la couleur qui lui est attribuée et s'il est vainqueur"""

    def __init__(self, name, players_pair):

        self.name = name
        self.winner = ""
        self.player1 = players_pair[0]
        self.player2 = players_pair[1]
        self.score_player1 = 0
        self.color_player1 = ""
        self.score_player2 = 0
        self.color_player2 = ""

    def __repr__(self) -> str:
        """La méthode __repr__ permet de représenter l'instance de la class Match sous forme de chaîne de caractères"""

        return (
            [self.player1, self.score_player1],
            [self.color_player2, self.score_player2],
        )

    def assign_colors(self):

        """Fonction d'assignation des couleurs aux joueurs"""
        if random.choice([True, False]):

            self.color_player1 = "Blanc"
            self.color_player2 = "Noir"

        else:
            self.color_player1 = "Noir"
            self.color_player2 = "Blanc"

    def play_match(self):

        """Fonction au démarrage du match on assigne une couleur aux joueurs de manière aléatoire"""

        self.assign_colors()

        print()
        winner = CheckView().get_user_entry(
            message_display=f"{self.player1.first_name} ({self.color_player1}) contre "
            + f"{self.player2.first_name} ({self.color_player2})\n"
            f"---Qui est le vainqueur ?---\n\n"
            f"1 - {self.player1.first_name} ({self.color_player1})\n"
            f"2 - {self.player2.first_name} ({self.color_player2})\n"
            f"3 - Égalité\n",
            message_error="Veuillez entrer 1, 2 ou 3.",
            value_type="selection",
            user_entry=["1", "2", "3"],
        )

        if winner == "0":
            self.winner = self.player1.first_name
            self.score_player1 += 1

        elif winner == "1":
            self.winner = self.player2.first_name
            self.score_player2 += 1

        elif winner == "2":
            self.winner = "Égalité"
            self.score_player1 += 0.5
            self.score_player2 += 0.5

        self.player1.tournament_score += self.score_player1
        self.player2.tournament_score += self.score_player2

    def get_serialized_match(self):
        return {
            "player1": self.player1.get_serialized_player(save_tournament_score=True),
            "score_player1": self.score_player1,
            "color_player1": self.color_player1,
            "player2": self.player2.get_serialized_player(save_tournament_score=True),
            "score_player2": self.score_player2,
            "color_player2": self.color_player2,
            "winner": self.winner,
            "name": self.name,
        }
