# Generated by Django 5.1.1 on 2024-12-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_alter_tournament_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_date',
            field=models.DateField(),
        ),
    ]
