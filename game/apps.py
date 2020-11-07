from django.apps import AppConfig


class GameConfig(AppConfig):
    name = "game"
    verbose_name = "Game"
    verbose_name_plural = "Games"

    def ready(self):
        import game.signals  # noqa
