# Generated by Django 2.2.12 on 2020-12-25 17:50

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part4', '0023_auto_20201225_2046'),
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
            field=otree.db.models.IntegerField(default=4, null=True),
        ),
    ]
