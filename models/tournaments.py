class Tournaments:
    
    def __init__(self, players='', tours=[], name='', place ='', date='', number_of_turns=[], time = ['bullet', 'blitz', 'coup rapide'], description=''):

        self.players = players
        self.tours = tours
        self.name = name
        self.place = place
        self.date = date
        self.number_of_turns = number_of_turns
        self.time = time
        self.description = description