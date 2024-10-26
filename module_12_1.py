import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_wolk(self):
        jogger = runner.Runner('Jon')
        for _ in range(10):
            jogger.walk()
        self.assertEqual(jogger.distance, 50)

    def test_run(self):
        jogger = runner.Runner('Pit')
        for _ in range(10):
            jogger.run()
        self.assertEqual(jogger.distance, 100)

    def test_challenge(self):
        jogger_first = runner.Runner('Martin')
        jogger_second = runner.Runner('Ben')
        for _ in range(10):
            jogger_first.run()
            jogger_second.walk()
        self.assertNotEqual(jogger_first.distance, jogger_second.distance)


if __name__ == "__main__":
    unittest.main()