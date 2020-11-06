from enum import IntEnum
from django.db import models
from django_mysql.models import JSONField

from internal.utils import empty_list
from .game import Minesweeper


class GameStatuses(IntEnum):
    """ Enum was used as choices of Game.status because explicit is better than implicit """

    NOT_PLAYED = 0
    PLAYING = 1
    FINISHED = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Game(models.Model):
    created_at = models.DateTimeField("Creation date", auto_now_add=True)
    modified_at = models.DateTimeField("Last update", auto_now=True)

    rows = models.PositiveIntegerField(
        "Board rows", default=10, help_text="Board's total rows"
    )
    cols = models.PositiveIntegerField(
        "Board cols", default=10, help_text="Board's total columns"
    )
    mines = models.PositiveIntegerField(
        "Mines on board", default=5, help_text="Board's total placed mines"
    )

    board = JSONField(
        "Generated board", default=empty_list, help_text="Whe generated board game"
    )
    win = models.BooleanField(
        "Win?",
        default=None,
        null=True,
        blank=True,
        help_text="Did the user win the game?",
    )
    status = models.IntegerField(
        choices=GameStatuses.choices(),
        default=GameStatuses.NOT_PLAYED,
        help_text="Actual game status",
    )

    def save(self, *args, **kwargs):
        """ If the board was not defined, we create a new as default """

        if not self.board:
            ms = Minesweeper(self.rows, self.cols, self.mines)
            ms.create_board()
            ms.put_mines()
            self.board = ms.board

        super(Game, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        db_table = "games"
