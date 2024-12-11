import unittest


def check_is_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @check_is_frozen
    def test_run(self):
        self.assertEqual(2 + 2, 4)

    @check_is_frozen
    def test_walk(self):
        self.assertEqual(3 + 3, 6)

    @check_is_frozen
    def test_challenge(self):
        self.assertEqual(5 * 5, 25)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @check_is_frozen
    def test_first_tournament(self):
        self.assertEqual(10 - 5, 5)

    @check_is_frozen
    def test_second_tournament(self):
        self.assertEqual(15 / 3, 5)

    @check_is_frozen
    def test_third_tournament(self):
        self.assertEqual(4 * 4, 16)
