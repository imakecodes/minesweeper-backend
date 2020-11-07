from django.contrib import admin

from .models import Game, GameEvent


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "modified_at",
        "rows",
        "cols",
        "mines",
        "win",
        "status",
    )

    list_filter = (
        "win",
        "status",
    )


@admin.register(GameEvent)
class GameEventAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "game", "type", "row", "col")

    list_filter = ("type",)
