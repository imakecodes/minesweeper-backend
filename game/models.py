from django.db import models
from django_mysql.models import JSONField

from internal.utils import empty_list
from .game import Minesweeper


class Game(models.Model):
    created_at = models.DateTimeField("Creation date", auto_now_add=True)
    modified_at = models.DateTimeField("Last update", auto_now=True)

    rows = models.PositiveIntegerField("Board rows", default=10)
    cols = models.PositiveIntegerField("Board cols", default=10)
    mines = models.PositiveIntegerField("Mines on board", default=5)

    board = JSONField("Generated board", default=empty_list)

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
