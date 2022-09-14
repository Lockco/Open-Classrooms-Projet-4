from models.round__models import Round


class Tournaments:
    def __init__(
        self,
        name,
        place,
        date,
        time_control,
        players,
        number_of_rounds=4,
        description="",
    ):

        self.name = name
        self.place = place
        self.date = date
        self.time_control = time_control
        self.players = players
        self.number_of_rounds = number_of_rounds
        self.rounds = []
        self.description = description

    def __str__(self):

        return f"Tournoi: {self.name}"

    def create_round(self, round_number):
        """Création du round"""

        players_pairs = self.create_players_pairs(current_round=round_number)
        round = Round("Round " + str(round_number + 1), players_pairs)
        self.rounds.append(round)

    def create_players_pairs(self, current_round):
        """Création des paires de joueurs"""

        if current_round == 0:
            sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)

        else:
            sorted_players = []
            score_sorted_players = sorted(
                self.players, key=lambda x: x.total_score, reverse=True
            )

            """Dans le cas où il y a deux joueurs qui ont le même score, on les trie en fonction de leur rang"""
            for i, player in enumerate(score_sorted_players):

                try:
                    sorted_players.append(player)

                except player.total_score == score_sorted_players[i + 1].total_score:

                    if player.ranking > score_sorted_players[i + 1].ranking:

                        higther_player = player
                        lower_player = score_sorted_players[i + 1]

                    else:

                        higther_player = score_sorted_players[i + 1]
                        lower_player = player

                    sorted_players.append(higther_player)
                    sorted_players.append(lower_player)

                except IndexError:
                    sorted_players.append(player)

        superior_part = sorted_players[len(sorted_players) // 2:]
        inferior_part = sorted_players[: len(sorted_players) // 2]

        players_pairs = []

        # On créé les pairs de joueurs
        for i, player in enumerate(superior_part):
            a = 0
            while True:

                try:
                    player2 = inferior_part[i + a]
                # On assigne le joueur 1 au dernier joueur de la liste inférieur
                except IndexError:
                    player2 = inferior_part[i]
                    print(f"{player2}")
                    players_pairs.append((player, player2))

                # On assigne les joueurs dans la liste qui leur corresponde
                # afin d'indiquer qu'ils on déjà joué l'un contre l'autre
                    player.opponent.append(player2)
                    player2.opponent.append(player)
                    break

                # Dans le cas où le joueur 1 a déjà joué contre le joueur 2, on test avec le joueur suivant
                if player in player2.opponent:
                    a += 1
                    continue

                # Dans le cas où les 2 joueurs n'ont pas encore joué l'un contre l'autre, alors on va créer une pair.
                # On n'oubli pas d'indiquer les adversaires dans la liste opponent des joueurs.
                else:
                    players_pairs.append((player, player2))
                    player.opponent.append(player2)
                    player2.opponent.append(player)
                    break

        return players_pairs

    def get_rankings(self, by_score=True):
        """Par défaut on va retourner le classement du tournois en fonction des points marqués par chaque joueurs"""

        if by_score:
            sorted_players = sorted(
                self.players, key=lambda x: x.tournament_score, reverse=True
            )

        else:
            sorted_players = sorted(self.players, key=lambda x: x.rank, reverse=True)

        return sorted_players

    def get_serialized_tournament(self, save_rounds=False):
        """Lorsqu'on sauvegarde suite à la création, les rounds ne sont pas encore créés."""

        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "time_control": self.time_control,
            "players": [
                player.get_serialized_player(save_tournament_score=True)
                for player in self.players
            ],
            "number_of_rounds": self.number_of_rounds,
            "rounds": [round.get_serialized_round() for round in self.rounds],
            "description": self.description,
        }

        if save_rounds:
            serialized_tournament["rounds"] = [
                round.get_serialized_round() for round in self.rounds
            ]

        return serialized_tournament
