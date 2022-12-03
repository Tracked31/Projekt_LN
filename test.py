from Game_Controller import GameController
import unittest
from unittest import mock
from unittest.mock import patch


class Test_Controller(unittest.TestCase):

    def setUp(self):
        self.test_control = GameController()

    def test_space_is_empty(self):
        self.assertEqual(self.test_control.space_is_empty(self.test_control.model.board(), 8), True)
        self.assertEqual(self.test_control.space_is_empty(self.test_control.model.board(), 0), True)
        with self.assertRaises(IndexError):
            self.test_control.space_is_empty(self.test_control.model.board(), 9)

    def test_get_winner_1(self):
        self.assertEqual(self.test_control.get_winner_1(["X", "X", "X", "_", "_", "_", "_", "_", "_"], 'X'), True) #first row
        self.assertEqual(self.test_control.get_winner_1(["_", "_", "_", "X", "X", "X", "_", "_", "_"], 'X'), True) #second row
        self.assertEqual(self.test_control.get_winner_1(["_", "_", "_", "_", "_", "_", "X", "X", "X"], 'X'), True) #third row
        self.assertEqual(self.test_control.get_winner_1(["X", "_", "_", "X", "_", "_", "X", "_", "_"], 'X'), True) #first column
        self.assertEqual(self.test_control.get_winner_1(["_", "X", "_", "_", "X", "_", "_", "X", "_"], 'X'), True) #second column
        self.assertEqual(self.test_control.get_winner_1(["_", "_", "X", "_", "_", "X", "_", "_", "X"], 'X'), True) #third column
        self.assertEqual(self.test_control.get_winner_1(["X", "_", "_", "_", "X", "_", "_", "_", "X"], 'X'), True) #first diagonal
        self.assertEqual(self.test_control.get_winner_1(["_", "_", "X", "_", "X", "_", "X", "_", "_"], 'X'), True) #second diagonal

        self.assertEqual(self.test_control.get_winner_1(["O", "O", "O", "_", "_", "_", "_", "_", "_"], 'O'), True) #first row
        self.assertEqual(self.test_control.get_winner_1(["_", "_", "_", "O", "O", "O", "_", "_", "_"], 'O'), True) #second row
        self.assertEqual(self.test_control.get_winner_1(["_", "_", "_", "_", "_", "_", "O", "O", "O"], 'O'), True) #third row
        self.assertEqual(self.test_control.get_winner_1(["O", "_", "_", "O", "_", "_", "O", "_", "_"], 'O'), True) #first column
        self.assertEqual(self.test_control.get_winner_1(["_", "O", "_", "_", "O", "_", "_", "O", "_"], 'O'), True) #second column
        self.assertEqual(self.test_control.get_winner_1(["_", "_", "O", "_", "_", "O", "_", "_", "O"], 'O'), True) #third column
        self.assertEqual(self.test_control.get_winner_1(["O", "_", "_", "_", "O", "_", "_", "_", "O"], 'O'), True) #first diagonal
        self.assertEqual(self.test_control.get_winner_1(["_", "_", "O", "_", "O", "_", "O", "_", "_"], 'O'), True) #second diagonal

    def test_is_draw(self):
        self.assertEqual(self.test_control.is_draw(["X", "O", "O", "O", "X", "X", "X", "X", "O"], 'X'), True)#board full
        self.assertEqual(self.test_control.is_draw(["X", "X", "X", "_", "O", "_", "_", "_", "O"], 'X'), False)#X is winner

    def test_is_over(self):
        self.assertEqual(self.test_control.is_over(["_", "_", "_", "_", "_", "_", "_", "_", "_"]), False)
        self.assertEqual(self.test_control.is_over(["X", "O", "X", "O", "O", "X", "X", "X", "O"]), True)

    @patch('Game_View.GameView.select_slot')
    def test_make_move(self, mock_select_slot):
        mock_select_slot.return_value = 0
        self.assertEqual(self.test_control.make_move(["_", "_", "_", "_", "_", "_", "_", "_", "_"], 'X'),
                         ["X", "_", "_", "_", "_", "_", "_", "_", "_"])
        self.assertEqual(self.test_control.make_move(["X", "_", "_", "_", "_", "_", "_", "_", "_"], 'X'),
                         self.test_control.view.pos_taken())

    def test_minmax_alg(self):
        val1 = self.test_control.minmax_alg(["X", "_", "_", "_", "_", "_", "_", "_", "_"], 'O')
        print(val1)

    def test_make_best_move(self):
        pass

    def test_computer_move(self):
        # bei vollem board testen?
        pass

    def test_save_game(self):
        fake_file_path = "game_data.json"
        self.test_control.model.board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        with patch('builtins.open', mock.mock_open()) as mocked_file:
            self.test_control.save_game()

            mocked_file.assert_called_once_with(fake_file_path, 'w')
            mocked_file.write.assert_called_once_with(self.test_control.model.board)

    def test_load_game(self):
        self.test_control.model.board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        mock_open_function = mock.mock_open(read_data=self.test_control.model.board)
        with mock.patch('builtins.open', mock_open_function):
            self.assertEqual(self.test_control.load_game(), "X")
            self.assertEqual(self.test_control.model.board, ["_", "_", "_", "_", "_", "_", "_", "_", "_"])


if __name__ == '__main__':
    unittest.main()
