# Generated by Django 2.2.12 on 2020-12-25 11:06

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0007_auto_20201225_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround1',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
    ]
