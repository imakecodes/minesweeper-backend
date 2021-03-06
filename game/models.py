from enum import IntEnum
from django.db import models
from django_mysql.models import JSONField

from internal.utils import empty_list
from .game import Minesweeper


class EnumChoicesBase(IntEnum):
    """ Enum was used as choices of Game.status because explicit is better than implicit """

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class GameStatuses(EnumChoicesBase):
    """ Statuses used by the player and system on game """

    NOT_PLAYED = 0
    PLAYING = 1
    PAUSED = 2
    FINISHED = 3


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
        "Generated board", default=empty_list, help_text="The generated board game"
    )
    board_progress = JSONField(
        "Progress board",
        default=empty_list,
        help_text="This board is updated at each GameEvent recorded",
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
            self.board_progress = ms.board_progress

        super(Game, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        db_table = "games"


class EventTypes(EnumChoicesBase):
    """ Event types to generate a game timeline """

    START_GAME = 0
    PAUSE = 1
    RESUME = 2
    CLICK_MINE = 3
    CLICK_POINT = 4
    CLICK_EMPTY = 5
    CLICK_FLAG = 6
    GAME_OVER = 7
    CLICK_NAIVE = 8


class GameEvent(models.Model):
    created_at = models.DateTimeField("Creation date", auto_now_add=True)
    game = models.ForeignKey("game.Game", on_delete=models.CASCADE)

    type = models.IntegerField(
        choices=EventTypes.choices(),
        default=EventTypes.CLICK_NAIVE,
        help_text="The game event",
    )

    row = models.PositiveIntegerField(
        "The row clicked",
        default=None,
        null=True,
        blank=True,
        help_text="Row on the board where the event occurred, if applicable",
    )
    col = models.PositiveIntegerField(
        "The column clicked",
        default=None,
        null=True,
        blank=True,
        help_text="Column on the board where the event occurred, if applicable",
    )

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Game event"
        verbose_name_plural = "Game events"
        db_table = "game_events"
