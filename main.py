from Game_Controller import GameController
from Game_View import GameView


class main_game:
    game: GameController
    view: GameView

    def __init__(self):
        self.game = GameController()
        self.view = GameView()

    def main(self):
        self.view.board()

        self.view.welcome_game()

        self.game.state_loader()

        if self.view.game_mode():
            self.game.mode_player()

        if not self.view.game_mode():
            self.game.mode_AI()


m = main_game.main()
