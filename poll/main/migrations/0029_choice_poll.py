# Generated by Django 2.2.1 on 2021-01-19 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice_poll_rel', to='main.Poll'),
        ),
    ]
