from Game_View import GameView
from Game_Model import GameModel
from math import inf
import json


class GameController:
    model: GameModel
    view: GameView

    def __init__(self):
        self.model: GameModel = GameModel()
        self.view: GameView = GameView(self.model)

    def space_is_empty(self, board: list[str], pos: int) -> bool:
        if board[pos] == "_":
            return True
        else:
            return False

    def get_winner_1(self, board: list[str], current_play: str) -> bool:
        if ((board[0] == current_play and board[1] == current_play and board[2] == current_play) or
                (board[3] == current_play and board[4] == current_play and board[5] == current_play) or
                (board[6] == current_play and board[7] == current_play and board[8] == current_play) or
                (board[0] == current_play and board[3] == current_play and board[6] == current_play) or
                (board[1] == current_play and board[4] == current_play and board[7] == current_play) or
                (board[2] == current_play and board[5] == current_play and board[8] == current_play) or
                (board[0] == current_play and board[4] == current_play and board[8] == current_play) or
                (board[2] == current_play and board[4] == current_play and board[6] == current_play)):
            return True
        return False

    def is_draw(self, board: list[str], current_play: str) -> bool:
        return self.is_over(board) or self.get_winner_1(self.model.board(), current_play)

    def is_over(self, board: list[str]) -> bool:
        return "_" not in board

    def make_move(self, board, current_play: str):
        while True:
            player_inp = self.view.select_slot()
            if self.space_is_empty(board, player_inp):
                board[player_inp] = self.model.current_player()
                break
            else:
                self.view.pos_taken()

        self.view.print_board(board)

    def minmax_alg(self, board, maximising) -> int:
        current_score = None

        if self.is_draw(self.model.board(), "O") is True:
            current_score = 0

        if self.is_draw(self.model.board(), "X") is True:
            current_score = 0

        if self.get_winner_1(self.model.board(), "O") is True:
            current_score = +1000

        if self.get_winner_1(self.model.board(), "X") is True:
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
                if self.space_is_empty(self.model.board(), move):
                    board[move] = "X"
                    util = self.minmax_alg(self.model.board(), False)
                    board[move] = "_"
                    best = max(util, best)
            return best

        else:
            best = +inf
            for move, _ in enumerate(board):
                if self.space_is_empty(self.model.board(), move):
                    board[move] = "O"
                    util = self.minmax_alg(self.model.board(), True)
                    board[move] = "_"
                    best = min(util, best)
            return best

    def make_best_move(self, board):
        best_score = -inf
        best_move = None
        for move, _ in enumerate(board):
            if self.space_is_empty(self.model.board(), move):
                board[move] = "O"
                score = self.minmax_alg(self.model.board(), True)
                board[move] = "_"
                if score > best_score:
                    best_move = move
                    best_score = score
        return best_move

    def computer_move(self, board):
        move = self.make_best_move(self.model.board())
        if self.space_is_empty(self.model.board(), move):
            board[move] = self.model.current_player()
        self.view.print_board(self.model.board())

    def state_loader(self):
        load_state = self.view.state_inp()
        if load_state == 1:
            return True
        else:
            return False

    def save_game(self):
        json_data = {
            "board": self.model.board()
        }
        with open("game_data.json", "w") as file:
            json.dump(json_data, file)

    def exit_game(self):
        ex_game = self.view.exit_inp()
        if ex_game == "ex":
            self.save_game()
            return True

    def load_game(self):
        with open("game_data.json", "r") as file:

            data = json.load(file)
            new_board = data["board"]
            self.model._board = new_board
            self.view.print_board(self.model.board())
            count_X = 0
            count_O = 0
            for element in new_board:
                if element == "O":
                    count_X += 1
                if element == "X":
                    count_O += 1

            if count_O > count_X:
                load_current1 = "X"
                return load_current1
            elif count_X > count_O:
                load_current2 = "O"
                return load_current2
            elif count_X == count_O:
                load_current3 = "X"
                return load_current3

    def mode_player(self):
        if self.state_loader():
            self.model.current_play = self.load_game()
        else:
            self.view.print_board(self.model.board())

        while True:
            self.make_move(self.model.board(), self.model.current_play)
            if self.is_over(self.model.board()):
                self.view.draw_output()
                break
            if self.get_winner_1(self.model.board(), self.model.current_play):
                self.view.win_output()
                break
            if self.exit_game():
                break
            self.model.swap_player()

    def mode_AI(self):
        if self.state_loader() == 1:
            self.model.current_play = self.load_game()
        else:
            self.view.print_board(self.model.board())
        while True:
            if self.model.current_player() == "X":
                self.make_move(self.model.board(), self.model.current_player())
            else:
                self.computer_move(self.model.board())
            if self.get_winner_1(self.model.board(), self.model.current_player()):
                self.view.win_output()
                break
            if self.is_over(self.model.board()):
                self.view.draw_output()
                break
            if self.exit_game():
                break
            self.model.swap_player()

    def main(self):
        self.model.board()
        self.view.welcome_game()
        self.model.mode = self.view.mode_inp()
        if self.model.mode == 0:
            self.mode_player()
        else:
            self.mode_AI()
