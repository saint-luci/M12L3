from Runner import Runner
import unittest

class RunnerTest(unittest.TestCase):

    isFrozen = False

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_walk(self):
        runner = Runner("Petr")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_run(self):
        runner = Runner("Petr")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(isFrozen, "Tests are frozen")
    def test_challenge(self):
        runner1 = Runner("Petr")
        runner2 = Runner("Petr2")
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()
