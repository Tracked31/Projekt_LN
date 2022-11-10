import unittest
from Game_Controller import GameController
from Game_Model import GameModel


class Test_Controller(unittest.TestCase):

    def __init__(self):
        test_model = GameModel()
        test_control = GameController()

    def test_space_is_empty(self):
        result = GameController.space_is_empty(self, GameModel.board(self), 10)
        self.assertTrue(result, False)

if __name__ == '__main__':
    unittest.main()
