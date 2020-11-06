from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Game, GameEvent, EventTypes
from .game import Minesweeper


@receiver(post_save, sender=Game)
def game_start(sender, signal, instance, **kwargs):
    """ If the game was just created, insert the first event START_GAME """

    GameEvent.objects.get_or_create(game=instance, type=EventTypes.START_GAME)


@receiver(pre_save, sender=GameEvent)
def identify_click_event(sender, signal, instance, **kwargs):
    """ Verify what is on the naive click: mine, point or empty """
    if not instance.type == EventTypes.CLICK_NAIVE:
        return

    ms = Minesweeper(
        instance.game.rows,
        instance.game.cols,
        instance.game.mines,
        instance.game.board,
    )

    if ms.is_mine(instance.metadata["row"], instance.metadata["col"]):
        instance.type = EventTypes.CLICK_MINE

    elif ms.is_empty(instance.metadata["row"], instance.metadata["col"]):
        instance.type = EventTypes.CLICK_EMPTY

    elif ms.is_point(instance.metadata["row"], instance.metadata["col"]):
        instance.type = EventTypes.CLICK_POINT
