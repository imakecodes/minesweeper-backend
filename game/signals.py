from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Game, GameEvent, EventTypes


@receiver(post_save, sender=Game)
def game_start(sender, signal, instance, **kwargs):
    """ If the game was just created, insert the first event START_GAME """

    GameEvent.objects.get_or_create(game=instance, type=EventTypes.START_GAME)
