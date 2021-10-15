# Phil Dreizen
# Tic Tac Toe

EMPTY = 0
X = 1
O = 2


NROWS = 3
NCOLS = 3

START_POS = 0
MAX_ROW_POS = NROWS - 1
MAX_COL_POS = NCOLS - 1


class Board:
    def __init__(self):
        self.b = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    
    @staticmethod
    def val_to_str(val):
        """
        str representation of a cell's value
        """
        if val == X:
            return "X"
        elif val == O:
            return "O"
        else:
            return " "

    def __getitem__(self, key):
        """
        return value of a cell via a tuple (row, col)
        """
        return self.b[key[0]][key[1]]

    def __setitem__(self, key, val):
        """
        set value of a cell via a tuple (row, col)
        """
        self.b[key[0]][key[1]] = val

    def is_empty(self, key):
        """
        is the cell at (row, col) empty?
        """
        return self[key] == EMPTY

    def is_in_bounds(self, move):
        row_pos, col_pos = move
        return START_POS <= row_pos <= MAX_ROW_POS and START_POS <= col_pos <= MAX_COL_POS

    def is_valid(self, move):
        """
        is the move valid, given the current state of the board?
        """
        if move is None:
            return False
        return self.is_in_bounds(move) and self.is_empty(move)

    def is_full(self):
        return all([all(row) for row in self.b])
    
    def check_win(self):
        """
        Are we in a win state?
        """
        b = self.b

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

    def __repr__(self):
        s = ''
        for r in range(3):
            for c in range(3):
                s += f'{self.val_to_str(self.b[r][c])}'
                s += '|' if c < 2 else '\n'
        return s


class Player:
    def __init__(self, val):
        self.val = val  # X or O

    def _from_console(self, board):
        """
        Ask player to choose move.
        Reads in cell as row and column like: 01, 22
        TODO: maybe make each cell a single number: 1,2,3,...9
        """
        rc = input(f'Player {board.val_to_str(self.val)} Select Move: ')
        try:
            return int(rc[0]), int(rc[1])
        except ValueError:
            return None

    def choose_move(self, board):
        move = self._from_console(board)
        while not board.is_valid(move):
            print("Invalid move.")
            move = self._from_console(board)

        return move


class Game:
    def __init__(self):
        self.board = Board()
        self.playerX = Player(X)
        self.playerO = Player(O)
        self.current_player = self.playerX

    def start(self):
        winner = None
        while not winner and not self.board.is_full():
            print(self.board)
            
            move = self.current_player.choose_move(self.board)
            self.board[move] = self.current_player.val

            if self.board.check_win():
                winner = self.current_player
            else:
                # swap current_player
                self.current_player = self.playerX if self.current_player == self.playerO else self.playerO

        print(self.board)
        if winner:
            print(f'The winner is Player {self.board.val_to_str(winner.val)}')
        else:
            print("The game is a draw")


if __name__ == '__main__':
    game = Game()
    game.start()

