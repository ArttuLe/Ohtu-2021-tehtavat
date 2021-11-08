import unittest
from statistics import Statistics
from statistics import sort_by_points
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_etsi_pelaaja(self):
        pelaaja = self.statistics.search("Kurri")

        self.assertEqual(pelaaja.name,"Kurri")

    def test_etsi_olematon_pelaaja(self):

        pelaaja = self.statistics.search("Antero")

        self.assertEqual(None,None)       

    def test_hae_pisteet(self):
        pelaaja = self.statistics.search("Kurri")
        points = sort_by_points(pelaaja)
        self.assertEqual(points,90)

    def test_hae_joukkue(self):
        joukkue = self.statistics.team("EDM")
        names = []
        for player in joukkue:
            names.append(player.name)
        
        result = ["Semenko", "Kurri","Gretzky"]
        self.assertEqual(names, result)

    def test_hae_top_score(self):

        top3 = self.statistics.top_scorers(2)
        result = []
        for player in top3:
            result.append(sort_by_points(player))
        self.assertEqual(result, [124,99,98])


    