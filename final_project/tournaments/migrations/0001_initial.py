# Generated by Django 5.1.1 on 2024-12-18 14:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0003_team_logo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('stadium_place', models.CharField(max_length=100)),
                ('entry_fee', models.PositiveIntegerField()),
                ('teams_quantity', models.PositiveIntegerField()),
                ('organizers', models.ManyToManyField(related_name='organized_tournaments', to=settings.AUTH_USER_MODEL)),
                ('teams', models.ManyToManyField(to='team.team')),
            ],
        ),
    ]
