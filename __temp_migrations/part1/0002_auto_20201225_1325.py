# Generated by Django 2.2.12 on 2020-12-25 10:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='payround1',
            field=otree.db.models.IntegerField(default=3, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=7, null=True),
        ),
    ]
