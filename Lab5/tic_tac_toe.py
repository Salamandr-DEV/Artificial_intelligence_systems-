from easyAI import TwoPlayerGame, AI_Player, Negamax
from easyAI.Player import Human_Player

class GameController(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.current_player = 1
        self.board = [0 for i in range(9)]

    def possible_moves(self):
        return [a + 1 for a, b in enumerate(self.board) if b == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player

    def loss_condition(self):
        possible_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                                 [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        return any([all([(self.board[i - 1] == self.opponent_index)
                         for i in combination]) for combination in possible_combinations])

    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    def show(self):
        print('\n' + '\n'.join([' '.join([['.', 'O', 'X'][self.board[3 * j + i]]
                                          for i in range(3)]) for j in range(3)]))

    def scoring(self):
        return -100 if self.loss_condition() else 0


if __name__ == "__main__":
    algorithm = Negamax(7)
    GameController([Human_Player(), AI_Player(algorithm)]).play()

