class Players :
    '''Création de l'objet joueur'''
    
    def __init__(self, first_name, surname, date_of_birth, gender, ranking = 0):

        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.total_score = 0
        self.tournament_score = 0
        self.ranking = ranking
        self.opponent = []
    
    print('Joueur créé. ')

    # def __str__(self):
        
    #     '''Retourne la représentation de l'objet en chaîne de caractères'''
    #     return f'{self.first_name} {self.surname} [{self.tournament_score}points]'

    # def get_serialized_player(self, save_tournament_score=False):

    #     serialized_player = {
    #         'first_name': self.first_name,
    #         'surname': self.surname,
    #         'date_of_birth': self.date_of_birth,
    #         'gender': self.gender,
    #         'ranking': self.ranking,
    #         'total_score': self.total_score

    #     }

