import operator

class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
        self.players = []
        self.players = self.reader.get_players()


    def top_scorers_by_nationality(self,nat):
        ret = []
        for player in sorted(self.players, key=operator.attrgetter('points'),reverse=True):
            if player.nationality == nat:
                ret.append(player)

        return ret