import unittest
from Game_Controller import GameController
from Game_Model import GameModel
from Game_View import GameView


class Test_Controller(unittest.TestCase):

    def setUp(self):
        self.test_model = GameModel()
        self.test_control = GameController()
        self.test_view = GameView(self.test_model)

    def test_space_is_empty(self):
        self.assertEqual(self.test_control.space_is_empty(self.test_model.board(), 10), False)
        self.assertEqual(self.test_control.space_is_empty(self.test_model.board(), 9), True)
        self.assertEqual(self.test_control.space_is_empty(self.test_model.board(), 0), True)

    def test_get_winner_1(self):
        self.assertTrue(self.test_control.get_winner_1(["X", "X", "X", "_", "_", "_", "_", "_", "_"], 'X')) #first row
        self.assertTrue(self.test_control.get_winner_1(["_", "_", "_", "X", "X", "X", "_", "_", "_"], 'X')) #second row
        self.assertTrue(self.test_control.get_winner_1(["_", "_", "_", "_", "_", "_", "X", "X", "X"], 'X')) #third row
        self.assertTrue(self.test_control.get_winner_1(["X", "_", "_", "X", "_", "_", "X", "_", "_"], 'X')) #first column
        self.assertTrue(self.test_control.get_winner_1(["_", "X", "_", "_", "X", "_", "_", "X", "_"], 'X')) #second column
        self.assertTrue(self.test_control.get_winner_1(["_", "_", "X", "_", "_", "X", "_", "_", "X"], 'X')) #third column
        self.assertTrue(self.test_control.get_winner_1(["X", "_", "_", "_", "X", "_", "_", "_", "X"], 'X')) #first diagonal
        self.assertTrue(self.test_control.get_winner_1(["_", "_", "X", "_", "X", "_", "X", "_", "_"], 'X')) #second diagonal

        self.assertTrue(self.test_control.get_winner_1(["O", "O", "O", "_", "_", "_", "_", "_", "_"], 'O')) #first row
        self.assertTrue(self.test_control.get_winner_1(["_", "_", "_", "O", "O", "O", "_", "_", "_"], 'O')) #second row
        self.assertTrue(self.test_control.get_winner_1(["_", "_", "_", "_", "_", "_", "O", "O", "O"], 'O')) #third row
        self.assertTrue(self.test_control.get_winner_1(["O", "_", "_", "O", "_", "_", "O", "_", "_"], 'O')) #first column
        self.assertTrue(self.test_control.get_winner_1(["_", "O", "_", "_", "O", "_", "_", "O", "_"], 'O')) #second column
        self.assertTrue(self.test_control.get_winner_1(["_", "_", "O", "_", "_", "O", "_", "_", "O"], 'O')) #third column
        self.assertTrue(self.test_control.get_winner_1(["O", "_", "_", "_", "O", "_", "_", "_", "O"], 'O')) #first diagonal
        self.assertTrue(self.test_control.get_winner_1(["_", "_", "O", "_", "O", "_", "O", "_", "_"], 'O')) #second diagonal

    def test_is_draw(self):
        self.assertTrue(self.test_control.is_draw(["X", "O", "O", "O", "X", "X", "X", "_", "O"], 'X'))#board not full and no winner
        self.assertTrue(self.test_control.is_draw(["X", "O", "O", "O", "X", "X", "X", "_", "O"], 'O'))#board not full and no winner
        self.assertTrue(self.test_control.is_draw(["X", "O", "O", "O", "X", "X", "X", "_", "O"], 'X'))#board full
        self.assertTrue(self.test_control.is_draw(["O", "O", "O", "_", "_", "_", "_", "_", "_"], 'O'))#board full

    def test_is_over(self):
        self.assertFalse(self.test_control.is_over(["_", "_", "_", "_", "_", "_", "_", "_", "_"]))
        self.assertTrue(self.test_control.is_over(["X", "O", "X", "O", "O", "X", "X", "X", "O"]))

    def test_make_move(self):
        # bei vollem board testen?
        # ob Position schon besetzt ist, check?
        pass

    def test_minmax_alg(self):
        pass

    def test_make_best_move(self):
        pass

    def test_computer_move(self):
        # bei vollem board testen?
        pass

    def test_state_loader(self):
        pass

    def test_save_game(self):
        pass

    def test_exit_game(self):
        pass

    def test_load_game(self):
        pass

    def test_mode_player(self):
        pass

    def test_mode_AI(self):
        pass

    def test_main(self):
        pass


if __name__ == '__main__':
    unittest.main()
