from Game_Model import GameModel


class GameView:
    model: GameModel

    def __init__(self):
        self.model = GameModel()

    def print_board(self, board: list):
        print(board[0] + "  |  " + board[1] + "  |  " + board[2])

        print("_____________")

        print(board[3] + "  |  " + board[4] + "  |  " + board[5])

        print("_____________")

        print(board[6] + "  |  " + board[7] + "  |  " + board[8])

    def select_slot(self) -> int:
        inp = None
        while 1 < inp < 10:
            try:
                inp = int(input("Select a number between 1-9 to make your move:"))
            except Exception as e:
                print(e)
        return inp-1

    def pos_taken(self):
        print("This position is already taken!")

    def in_range(self):
        print("Make sure that ur number is in the range of 1-9!")

    def welcome_game(self):
        print("Welcome to the World of Tic-Tac-Toe")

        print("The positions are shown as following:")
        print("1, 2, 3 ")
        print("4, 5, 6 ")
        print("7, 8, 9 ")
        print("")

    def state_inp(self):
        return input("If you want to load the games state from the last time you exited the game type 1:")

    def exit_inp(self):
        return input("If you want to exit the game type 'ex' and the game will save and close:")

    def mode_inp(self):
        inp = None
        while inp not in [0, 1]:
            try:
                inp = int(input("If you want to play against the computer type 1, "
                                "if you want to play against yourself type 0:"))
            except Exception as e:
                print(e)
        return inp
