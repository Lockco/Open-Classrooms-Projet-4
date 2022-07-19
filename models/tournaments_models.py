class Tournaments:
    
    def __init__(self, players='', name='', place ='', date='', number_of_turns=4, time = ['bullet', 'blitz', 'coup rapide'], description=''):

        self.name = name
        self.place = place
        self.date = date
        self.time = time
        self.players = players
        self.number_of_turns = number_of_turns
        self.description = description