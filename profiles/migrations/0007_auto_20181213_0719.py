# Generated by Django 2.0.9 on 2018-12-13 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20181213_0711'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CharacterClass',
        ),
        migrations.DeleteModel(
            name='CharacterFaction',
        ),
        migrations.DeleteModel(
            name='CharacterRace',
        ),
    ]
