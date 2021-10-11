# Phil Dreizen
# Tic Tac Toe

EMPTY = 0
X = 1
O = 2


class Board:
    def __init__(self):
        self.b = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

    @staticmethod
    def val_to_str(val):
        if val == X:
            return "X"
        elif val == O:
            return "O"
        else:
            return " "

    def is_valid(self, move):
        r, c = move
        return 0 <= r <= 2 and 0 <= c <= 2 and not self.b[r][c]

    def is_full(self):
        return all([all(row) for row in self.b])

    def __repr__(self):
        s = ''
        for r in range(3):
            for c in range(3):
                s += f'{self.val_to_str(self.b[r][c])}'
                s += '|' if c < 2 else '\n'
        return s


class Player:
    def __init__(self, val):
        self.val = val

    def make_move(self):
        rc = input(f'Player {Board.val_to_str(self.val)} Select Move: ')
        return int(rc[0]), int(rc[1])


class Game:
    def __init__(self):
        self.board = Board()
        self.playerX = Player(X)
        self.playerO = Player(O)
        self.current_player = self.playerO  # To be immediately swapped

    def is_win(self):
        b = self.board.b

        def is_row_win():
            for row in b:
                if row[0] and row[0] == row[1] and row[0] == row[2]:
                    return True
            return False

        def is_col_win():
            for c in range(3):
                if b[0][c] and b[0][c] == b[1][c] and b[0][c] == b[2][c]:
                    return True
            return False

        def is_diag1_win():
            return b[0][0] and b[0][0] == b[1][1] and b[0][0] == b[2][2]

        def is_diag2_win():
            return b[0][2] and b[0][2] == b[1][1] and b[0][2] == b[2][0]

        return is_row_win() or is_col_win() or is_diag1_win() or is_diag2_win()

    def start(self):
        winner = None
        while not winner and not self.board.is_full():
            self.current_player = self.playerX if self.current_player == self.playerO else self.playerO
            print(self.board)
            move = self.current_player.make_move()
            while not self.board.is_valid(move):
                print("Invalid move.")
                move = self.current_player.make_move()

            self.board.b[move[0]][move[1]] = self.current_player.val
            if self.is_win():
                winner = self.current_player

        print(self.board)
        if winner:
            print(f'The winner is Player {self.board.val_to_str(winner.val)}')
        else:
            print("The game is a draw")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.start()
