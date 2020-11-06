from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Game, GameEvent, EventTypes, GameStatuses
from .game import Minesweeper


@receiver(post_save, sender=Game)
def game_start(sender, signal, instance, **kwargs):
    """ If the game was just created, insert the first event START_GAME """
    if not instance.status == GameStatuses.NOT_PLAYED:
        return
    GameEvent.objects.get_or_create(game=instance, type=EventTypes.START_GAME)


@receiver(pre_save, sender=GameEvent)
def mark_game_as_playing(sender, signal, instance, **kwargs):
    """ When event match, mark the game instance as playing """

    playing_events = [
        EventTypes.START_GAME,
        EventTypes.RESUME,
        EventTypes.CLICK_MINE,
        EventTypes.CLICK_POINT,
        EventTypes.CLICK_EMPTY,
        EventTypes.CLICK_FLAG,
    ]

    if instance.type in playing_events:
        instance.game.status = GameStatuses.PLAYING
        instance.game.save()

    elif instance.type == EventTypes.PAUSE:
        instance.game.status = GameStatuses.PAUSED
        instance.game.save()

    if instance.type == EventTypes.CLICK_MINE:
        instance.game.status = GameStatuses.FINISHED
        instance.game.win = False
        instance.game.save()


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
