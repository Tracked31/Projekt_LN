from Game_View import GameView
from Game_Model import GameModel
from math import inf
import json


class GameController:
    game: GameModel
    view: GameView

    def __init__(self):
        self.game = GameModel()
        self.view = GameView()

    def space_is_empty(self, board, pos):
        if board[pos] == "_":
            return True
        else:
            return False

    def get_winner_1(self, board, current_play):
        if ((board[0] == current_play and board[1] == current_play and board[2] == current_play) or
            (board[3] == current_play and board[4] == current_play and board[5] == current_play) or
            (board[6] == current_play and board[7] == current_play and board[8] == current_play) or
            (board[0] == current_play and board[3] == current_play and board[6] == current_play) or
            (board[1] == current_play and board[4] == current_play and board[7] == current_play) or
            (board[2] == current_play and board[5] == current_play and board[8] == current_play) or
            (board[0] == current_play and board[4] == current_play and board[8] == current_play) or
            (board[2] == current_play and board[4] == current_play and board[6] == current_play)):
            return True

    def is_draw(self, board, current_play):
        if self.is_over(self.view.board()) == True or self.get_winner_1(self.view.board(), current_play) == True:
            return True
        else:
            return False

    def is_over(self, board):
        if "_" in board:
            return False
        else:
            return True

    def make_move(self, board, current_play):
        run = True
        while run:
            player_inp = self.view.input()
            if 1 <= player_inp <= 9:
                player_inp -= 1
                if self.space_is_empty(board, player_inp):
                    run = False
                    board[player_inp] = current_play
                else:
                    if not self.space_is_empty(board, player_inp):
                        self.view.pos_taken()
            else:
                run = False
                self.view.in_range()

        self.view.print_board(board)

    def minmax_alg(self, board, maximising):
        current_score = None

        if self.is_draw(self.view.board(), "O") is True:
            current_score = 0

        if self.is_draw(self.view.board(), "X") is True:
            current_score = 0

        if self.get_winner_1(self.view.board(), "O") is True:
            current_score = +1000

        if self.get_winner_1(self.view.board(), "X") is True:
            current_score = -1000

        if current_score == 1000:
            return current_score

        if current_score == -1000:
            return current_score

        if current_score == 0:
            return current_score

        if maximising:
            best = -inf
            for move, _ in enumerate(board):
                if self.space_is_empty(self.view.board(), move):
                    board[move] = "X"
                    util = self.minmax_alg(self.view.board(), False)
                    board[move] = "_"
                    best = max(util, best)
            return best

        else:
            best = +inf
            for move, _ in enumerate(board):
                if self.space_is_empty(self.view.board(), move):
                    board[move] = "O"
                    util = self.minmax_alg(self.view.board(), True)
                    board[move] = "_"
                    best = min(util, best)
            return best

    def mode_player(self):
        if self.state_loader() == 1:
            self.load_game()
        else:
            self.view.print_board(self.view.board())

        while True:

            if self.exit_game():
                break

            if self.is_over(self.view.board()):
                print("The Game ends in a draw!!!")
                break
            current_play = "X"
            if self.get_winner_1(self.view.board(), current_play):
                print("Player X has won the game!")
                break
            self.make_move(self.view.board(), current_play)

            if self.exit_game():
                break

            if self.is_over(self.view.board()):
                print("The game ends in a draw!!!")
                break
            current_play = "O"
            if self.get_winner_1(self.view.board(), current_play):
                print("Player O has won the game!")
                break
            self.make_move(self.view.board(), current_play)

    def mode_AI(self):
        if self.state_loader() == 1:
            self.load_game()
        else:
            self.view.print_board(self.view.board())

        while True:

            if self.exit_game():
                break

            current_play = "X"

            if self.is_over(self.view.board()):
                self.view.print_board(self.view.board())
                print("The game ends in a draw!!!")
                break
            self.make_move(self.view.board(), current_play)

            if self.get_winner_1(self.view.board(), current_play):
                print("Player X has won the game!")
                break

            if self.is_over(self.view.board()):
                self.view.print_board(self.view.board())
                print("The game ends in a draw!!!")
                break
            self.computer_move(self.view.board())

            if self.get_winner_1(self.view.board(), current_play):
                print("Player X has won the game!")
                break

    def make_best_move(self, board):
        best_score = -inf
        best_move = None
        for move, _ in enumerate(board):
            if self.space_is_empty(self.view.board(), move):
                board[move] = "O"
                score = self.minmax_alg(self.view.board(), True)
                board[move] = "_"
                if score > best_score:
                    best_move = move
                    best_score = score
        return best_move

    def computer_move(self, board):
        move = self.make_best_move(self.view.board())
        if self.space_is_empty(self.view.board(), move):
            board[move] = "O"
        print(board)
        self.view.print_board(self.view.board())

    def state_loader(self):
        load_state = self.view.state_inp()
        if load_state == 1:
            self.load_game()

    def exit_game(self):
        ex_game = self.view.exit_inp()
        if ex_game == "ex":
            self.save_game()

    def save_game(self):
        with open("game_data.json", "w") as file:
            json.dump(self.view.board(), file)

    def load_game(self):
        with open("game_date.json", "r") as file:
            json_str = json.load(file)
            print(json_str)
