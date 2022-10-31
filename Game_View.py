class GameView:

    def __init__(self):
        pass

    def board(self):
        board = ["_" for i in range(9)]


    def print_board(selfm, board):
        print(board[0] + "  |  " + board[1] + "  |  " + board[2])

        print("_____________")

        print(board[3] + "  |  " + board[4] + "  |  " + board[5])

        print("_____________")

        print(board[6] + "  |  " + board[7] + "  |  " + board[8])

    def input(self):
        return int(input("Select a number between 1-9 to make your move:"))

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

    def game_mode(self):
        run = True
        while run:
            mode = int(input("If you want to play against the computer type 1, "
                             "if you want to play against yourself type 0:"))
            if mode == 0:
                a = True
                return a
            elif mode == 1:
                a = False
                return a
        else:
            run = False
            print("Please select an available game mode!!! ")
