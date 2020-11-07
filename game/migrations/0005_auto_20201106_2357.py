# Generated by Django 3.1.3 on 2020-11-06 23:57

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0004_auto_20201106_0453"),
    ]

    operations = [
        migrations.RemoveField(model_name="gameevent", name="metadata",),
        migrations.AddField(
            model_name="gameevent",
            name="event_col",
            field=models.PositiveIntegerField(
                blank=True,
                default=None,
                help_text="Column on the board where the event occurred, if applicable",
                null=True,
                verbose_name="The column clicked",
            ),
        ),
        migrations.AddField(
            model_name="gameevent",
            name="event_row",
            field=models.PositiveIntegerField(
                blank=True,
                default=None,
                help_text="Row on the board where the event occurred, if applicable",
                null=True,
                verbose_name="The row clicked",
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="status",
            field=models.IntegerField(
                choices=[
                    (0, "NOT_PLAYED"),
                    (1, "PLAYING"),
                    (2, "PAUSED"),
                    (3, "FINISHED"),
                ],
                default=game.models.GameStatuses["NOT_PLAYED"],
                help_text="Actual game status",
            ),
        ),
    ]