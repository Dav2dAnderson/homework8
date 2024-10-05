# Generated by Django 5.1.1 on 2024-10-05 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('created_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('age', models.PositiveIntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=250)),
                ('score_first_team', models.PositiveIntegerField(default=0)),
                ('score_second_team', models.PositiveIntegerField(default=0)),
                ('sport_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sporttype')),
                ('first_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='first_team_games', to='main.team')),
                ('second_team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='second_team_games', to='main.team')),
            ],
        ),
    ]
