# Generated by Django 2.2.12 on 2020-12-25 17:44

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0022_auto_20201225_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround1',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=2, null=True),
        ),
    ]
