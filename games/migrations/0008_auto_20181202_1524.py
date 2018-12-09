# Generated by Django 2.0.9 on 2018-12-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20181020_1413'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='gamesession',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='gamesession',
            name='extra_players',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Additional players'),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='reported',
            field=models.BooleanField(default=False, verbose_name='Reported'),
        ),
    ]