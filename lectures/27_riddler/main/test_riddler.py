import unittest
from unittest.mock import Mock, patch, call
from riddler import Riddler


class RiddlerTestCase(unittest.TestCase):

    def setUp(self):
        self.riddler = Riddler()

    # тестируем метод add_riddle, все довольно просто
    def test_add_riddle_success(self):
        self.riddler.add_riddle('test', 'test')
        self.assertEqual(self.riddler.riddles['test'], 'test')

    def test_add_riddle_wrong_type(self):
        riddles_before = self.riddler.riddles.copy()
        self.riddler.add_riddle(123, 123)
        self.assertEqual(self.riddler.riddles, riddles_before)

    # как тестировать метод с пользовательским вводом? принтом? и рандомом?

    @patch('random.choice', Mock(return_value='Маленький, серенький, на слона похож.'))
    def test_riddle_print_question(self):
        with patch('sys.stdout', Mock()) as mock_print:
            self.riddler.riddle()
            mock_print.assert_has_calls(call('Маленький, серенький, на слона похож.'),
                                        call('У вас 3 попытки!'))

if __name__ == '__main__':
    unittest.main()  # если запускаем в нормальном месте
