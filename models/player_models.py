class Player:
    """Création de l'objet joueur"""

    def __init__(self, first_name, name, date_of_birth, gender, total_score, ranking=0):

        self.first_name = first_name
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.total_score = total_score
        self.tournament_score = 0
        self.ranking = ranking
        self.opponent = []

    def __str__(self):

        """Retourne la représentation de l'objet en chaîne de caractères"""
        return f"{self.first_name} {self.name} [{self.tournament_score} points]"

    def get_serialized_player(self, save_tournament_score=False):

        serialized_player = {
            "name": self.name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "total_score": self.total_score,
            "ranking": self.ranking,
        }
        if save_tournament_score:
            serialized_player["tournament_score"] = self.tournament_score

        return serialized_player
