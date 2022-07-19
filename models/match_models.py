class Match:

    '''dans l"init on peut préciser le nom du joueur, son score, la couleur qui lui est attribué et si il est vainqueur'''
    def __init__(self, name, players, score, color, winner, players_pair):

        self.name = name
        self.players = players
        
        pass
'''
    Fonction pour assigner une couleur à un joueur
'''  

'''
    Fonction pour demander le résultat du match à l'utilisateur
    
      on affiche les joueurs du match
      on demande quel joueur a gagné, on laisse 3 possibilité joueur1 remporte la partie, joueur2 remporte la partie ou égalité
      
      Si le joueur1 a gagné on lui ajoute 1 point
      Si le joueur2 a gagné on lui ajoute 1 point
      Si il y a égalité on ajoute 0.5 points au deux joueurs
'''

''' 
    On créer une fonction pour séréaliser le match qui return les informations suivante :
      
      le joueur1 et 2, leur score, leur couleur et le nom du gagnant
'''