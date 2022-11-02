class GameModel:
    _board: list[str] = []
    _players = ['X', 'O']
    _active = 'X'
    mode: int

    def __init__(self):
        self.reload()

    def board(self):
        return self._board

    def reload(self) -> None:
        self._board = ["_" for i in range(9)]

    def current_player(self, current_play) -> str:
        player1 = "X"
        player2 = "O"
        if current_play == player1:
            current_play = player2
        elif current_play == player2:
            current_play = player1
        return current_play
