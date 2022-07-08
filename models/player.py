from yaml import serialize


class Players :

    def __init__(self, first_name, surname, date_of_birth, gender,total_score,  ranking = 0):

        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.total_score = total_score
        self.ranking = ranking
    
    print('Joueur créé. ')

    def get_serialized_player(self, save_turnament_score=False):

        serialized_player = {
            'first_name': self.first_name,
            'surname': self.surname,
            'date_of_birth': self.date_of_birth,
            'gender': self.gender,
            'ranking': self.ranking,
            'total_score': self.total_score

        }
    