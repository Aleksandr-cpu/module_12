import logging
import unittest
from HumanMoveTest import rt_with_exceptions


class RunnerTest(unittest.TestCase):

    is_frozen = False
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            jogger = rt_with_exceptions.Runner('Jon', -5)
            for _ in range(10):
                jogger.walk()
            self.assertEqual(jogger.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            jogger = rt_with_exceptions.Runner(5, 5)
            for _ in range(10):
                jogger.run()
            self.assertEqual(jogger.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        jogger_first = rt_with_exceptions.Runner('Martin', 5)
        jogger_second = rt_with_exceptions.Runner('Ben',1)
        for _ in range(10):
            jogger_first.run()
            jogger_second.walk()
        self.assertNotEqual(jogger_first.distance, jogger_second.distance)


if __name__ == "__main__":
    unittest.main()