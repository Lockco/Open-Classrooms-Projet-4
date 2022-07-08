class players :

    def __init__(self, name='', surname='', date_of_birth='', gender = ['male', 'female'],  ranking = ''):

        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
    
    print('Joueur créé. ')