# Generated by Django 2.2.12 on 2020-12-27 09:13

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part4', '0034_auto_20201225_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='payround1',
            field=otree.db.models.IntegerField(default=3, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='payround2',
            field=otree.db.models.IntegerField(default=12, null=True),
        ),
    ]
