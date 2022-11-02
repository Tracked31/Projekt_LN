class GameModel:

    def __init__(self):
        pass

    def board(self):
        board = ["_" for i in range(9)]
        return board

    def current_player(self, current_play):
        player1 = "X"
        player2 = "O"
        if current_play == player1:
            current_play = player2
        elif current_play == player2:
            current_play = player1
        return current_play
