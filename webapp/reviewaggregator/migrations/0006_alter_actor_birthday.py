# Generated by Django 4.0.1 on 2022-01-23 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewaggregator', '0005_alter_actor_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата рождения'),
        ),
    ]