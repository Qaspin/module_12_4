import unittest
import logging
import rt_with_exceptions as rt


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            walker = rt.Runner('Евгений', -3)
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('Test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            runer = rt.Runner(1997)
            for i in range(10):
                runer.run()
            self.assertEqual(runer.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)




logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format="%(asctime)s | %(levelname)s | %(message)s | %(funcName)s | %(lineno)s")
