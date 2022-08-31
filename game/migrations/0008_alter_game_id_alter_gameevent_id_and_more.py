# Generated by Django 4.1 on 2022-08-30 23:20

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0007_auto_20201107_0130"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="gameevent",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="gameevent",
            name="type",
            field=models.IntegerField(
                choices=[
                    (0, "START_GAME"),
                    (1, "PAUSE"),
                    (2, "RESUME"),
                    (3, "CLICK_MINE"),
                    (4, "CLICK_POINT"),
                    (5, "CLICK_EMPTY"),
                    (6, "CLICK_FLAG"),
                    (7, "GAME_OVER"),
                    (8, "CLICK_NAIVE"),
                ],
                default=game.models.EventTypes["CLICK_NAIVE"],
                help_text="The game event",
            ),
        ),
    ]