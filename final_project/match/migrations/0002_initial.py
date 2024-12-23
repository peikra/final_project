# Generated by Django 5.1.1 on 2024-12-17 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('match', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchinvitation',
            name='from_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_invitations', to='team.team'),
        ),
        migrations.AddField(
            model_name='matchinvitation',
            name='to_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_invitations', to='team.team'),
        ),
    ]
