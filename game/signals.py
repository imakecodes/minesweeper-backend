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
def identify_click_event(sender, signal, instance, **kwargs):
    """ Verify what is on the naive click: mine, point or empty """
    if not instance.type == EventTypes.CLICK_NAIVE:
        return

    if instance.row is None and instance.col is None:
        return

    ms = Minesweeper(
        instance.game.rows,
        instance.game.cols,
        instance.game.mines,
        instance.game.board,
    )

    if ms.is_mine(instance.row, instance.col):
        instance.type = EventTypes.CLICK_MINE

    elif ms.is_empty(instance.row, instance.col):
        instance.type = EventTypes.CLICK_EMPTY

    elif ms.is_point(instance.row, instance.col):
        instance.type = EventTypes.CLICK_POINT


@receiver(post_save, sender=GameEvent)
def create_post_save_game_event(sender, signal, instance, **kwargs):
    ms = Minesweeper(
        instance.game.rows,
        instance.game.cols,
        instance.game.mines,
        instance.game.board,
        instance.game.board_progress,
    )
    game_changed = False

    reveal_events = [
        EventTypes.CLICK_POINT,
        EventTypes.CLICK_EMPTY,
        EventTypes.CLICK_MINE,
    ]
    if instance.type in reveal_events:
        ms.reveal(instance.row, instance.col)
        instance.game.board_progress = ms.board_progress
        game_changed = True

    playing_events = [
        EventTypes.START_GAME,
        EventTypes.RESUME,
        EventTypes.CLICK_POINT,
        EventTypes.CLICK_EMPTY,
        EventTypes.CLICK_FLAG,
    ]

    if instance.type in playing_events:
        instance.game.status = GameStatuses.PLAYING
        game_changed = True

    elif instance.type == EventTypes.PAUSE:
        instance.game.status = GameStatuses.PAUSED
        game_changed = True

    elif instance.type == EventTypes.CLICK_MINE:
        instance.game.status = GameStatuses.FINISHED
        instance.game.win = False
        game_changed = True

        GameEvent(game=instance.game, type=EventTypes.GAME_OVER).save()

    if ms.win() is True:
        instance.game.status = GameStatuses.FINISHED
        instance.game.win = True
        game_changed = True

    if game_changed is True:
        instance.game.save()
