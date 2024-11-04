import unittest
from HumanMoveTest import runner_and_tournament


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usein = runner_and_tournament.Runner("Усейн", 10)
        self.runner_andrey = runner_and_tournament.Runner("Андрей", 9)
        self.runner_nik = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testRunOne(self):
        self.tour = runner_and_tournament.Tournament(90, self.runner_usein, self.runner_nik)
        self.all_results = self.tour.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testRunTwo(self):
        self.tour = runner_and_tournament.Tournament(90, self.runner_andrey, self.runner_nik)
        self.all_results = self.tour.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testRunThree(self):
        self.tour = runner_and_tournament.Tournament(90, self.runner_usein, self.runner_andrey, self.runner_nik)
        self.all_results = self.tour.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Ник")
        TournamentTest.all_results[3] = self.all_results

if __name__ == "__main__":
    unittest.main()

