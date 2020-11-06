from django.test import TestCase

from ..game import Minesweeper


class MinesweeperTestCase(TestCase):
    def test_board_2x3x1(self):
        ms = Minesweeper(2, 3)
        ms.create_board()

        expected_board = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(ms.board, expected_board)

    def test_the_board_should_have_8_mines(self):
        expected_mines = 8
        ms = Minesweeper(10, 10, expected_mines)
        ms.create_board()
        ms.put_mines()

        located_mines = 0

        for row in ms.board:
            located_mines += row.count(-1)

        self.assertEqual(located_mines, expected_mines)

    def test_is_mine_on_0x1(self):
        ms = Minesweeper(2, 2, 1)
        ms.board = [[0, -1], [0, 0]]

        self.assertEqual(ms.is_mine(0, 1), True)

    def test_is_not_mine_on_1x1(self):
        ms = Minesweeper(2, 2, 1)
        ms.board = [[1, -1], [-1, 1]]

        self.assertEqual(ms.is_mine(1, 1), False)

    def test_is_point_is_not_on_the_board(self):
        ms = Minesweeper(2, 2, 1)
        ms.board = [[0, 0], [0, 0]]

        self.assertEqual(ms.is_point_in_board(2, 1), False)

    def test_is_point_is_on_the_board(self):
        ms = Minesweeper(2, 2, 1)
        ms.board = [[0, 0], [0, 0]]

        self.assertEqual(ms.is_point_in_board(1, 1), True)

    def test_pontuation_creation_around_one_mine(self):
        ms = Minesweeper(3, 3, 1)
        ms.board = [
            [0, 0, 0],
            [0, -1, 0],
            [0, 0, 0],
        ]

        expected_board = [
            [1, 1, 1],
            [1, -1, 1],
            [1, 1, 1],
        ]

        ms.create_mine_points(1, 1)

        self.assertEqual(ms.board, expected_board)

    def test_pontuation_creation_around_two_mines(self):
        ms = Minesweeper(3, 3, 1)
        ms.board = [
            [0, 0, 0],
            [0, -1, -1],
            [0, 0, 0],
        ]

        expected_board = [
            [1, 2, 2],
            [1, -1, -1],
            [1, 2, 2],
        ]

        ms.create_mine_points(1, 1)
        ms.create_mine_points(1, 2)

        self.assertEqual(ms.board, expected_board)
