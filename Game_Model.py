class GameModel:
    _board: list[str] = []
    _players = ['X', 'O']
    _active = 'X'
    current_play: str
    mode: int

    def __init__(self):
        self.reload()
        self.current_play = "X"

    def reload(self) -> None:
        self._board = ["_" for i in range(9)]

    def board(self) -> list[str]:
        return self._board

    def current_player(self) -> str:
        return self.current_play

    def swap_player(self):
        self.current_play = "X" if self.current_play == "O" else "O"
