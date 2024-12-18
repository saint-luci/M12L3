import unittest
from unittest_methods import TournamentTest
from unittest_own import RunnerTest

ST = unittest.TestSuite()
ST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
ST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ST)