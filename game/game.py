import random


class Minesweeper:
    board = []

    def __init__(self, rows=10, cols=10, mines=5, board=None, board_progress=None):
        self.rows = rows
        self.cols = cols
        self.mines = mines

        if board is not None:
            self.board = board

        if board_progress is not None:
            self.board_progress = board_progress

    def create_board(self):
        """ Creating the board cells with 0 as default value """
        self.board = [[0 for col in range(self.cols)] for row in range(self.rows)]
        self.board_progress = [
            ["-" for col in range(self.cols)] for row in range(self.rows)
        ]

    def put_mine(self):
        """Put a single mine  on the board.
        The mine have a -1 value just for reference
        """
        mine_position_row = random.randrange(0, self.rows)
        mine_position_col = random.randrange(0, self.cols)

        if self.is_mine(mine_position_row, mine_position_col):
            self.put_mine()

        self.board[mine_position_row][mine_position_col] = -1
        return mine_position_row, mine_position_col

    def put_mines(self):
        """ Put the desired amount of mines on the board """
        for mine in range(1, self.mines + 1):
            mine_position_row, mine_position_col = self.put_mine()

            self.create_mine_points(mine_position_row, mine_position_col)

    def create_mine_points(self, mine_position_row, mine_position_col):
        """Populate the board with points that sorrounds the mine.
        The reference used is the mine that was already placed"""

        # North
        self.increment_safe_point(mine_position_row - 1, mine_position_col)

        # North-east
        self.increment_safe_point(mine_position_row - 1, mine_position_col + 1)

        # East
        self.increment_safe_point(mine_position_row, mine_position_col + 1)

        # South-east
        self.increment_safe_point(mine_position_row + 1, mine_position_col + 1)

        # South
        self.increment_safe_point(mine_position_row + 1, mine_position_col)

        # South-west
        self.increment_safe_point(mine_position_row + 1, mine_position_col - 1)

        # West
        self.increment_safe_point(mine_position_row, mine_position_col - 1)

        # North-west
        self.increment_safe_point(mine_position_row - 1, mine_position_col - 1)

    def is_mine(self, row, col):
        """ Checks whether the given location have a mine """
        try:
            return self.board[row][col] == -1
        except IndexError:
            return False

    def is_empty(self, row, col):
        """ Checks whether the given location is empty """
        try:
            return self.board[row][col] == 0
        except IndexError:
            return False

    def is_point(self, row, col):
        """ Checks whether the given location have pontuation """
        try:
            return self.board[row][col] > 0
        except IndexError:
            return False

    def is_point_in_board(self, row, col):
        """ Checks whether the location is inside board """
        if row in range(0, self.rows) and col in range(0, self.cols):
            return True
        return False

    def increment_safe_point(self, row, col):
        """ Creates the mine's pontuation frame """

        # Ignores if the point whether not in the board
        if not self.is_point_in_board(row, col):
            return

        # Verify if the position have a mine on it
        if self.is_mine(row, col):
            return

        # Increment the value of the position becaus is close to some mine
        self.board[row][col] += 1

    def reveal(self, row, col):
        self.board_progress[row][col] = self.board[row][col]

    def win(self):
        """ Identify if the player won the game """
        unrevealed = 0
        for row in self.board_progress:
            for cell in row:
                if cell == "-":
                    unrevealed += 1
        if (unrevealed - self.mines) == 0:
            return True
