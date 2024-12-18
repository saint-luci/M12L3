from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

    isFrozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usein", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nik", 3)

    @classmethod
    def tearDownClass(cls):
        for runner in list(cls.all_results.values()):
            runner = {key: str(value) for key, value in runner.items()}
            print(runner)

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_first_tour(self):
        tour = Tournament(90, self.runner1, self.runner3)
        self.__class__.all_results["tour1"] = tour.start()
        self.assertTrue(list(self.__class__.all_results["tour1"].values())[-1] == "Nik")

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_second_tour(self):
        tour = Tournament(90, self.runner2, self.runner3)
        self.__class__.all_results["tour2"] = tour.start()
        self.assertTrue(list(self.__class__.all_results["tour2"].values())[-1] == "Nik")

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_third_tour(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.__class__.all_results["tour3"] = tour.start()
        self.assertTrue(list(self.__class__.all_results["tour3"].values())[-1] == "Nik")



if __name__ == "__main__":
    unittest.main()

