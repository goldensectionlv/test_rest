# Generated by Django 2.2.1 on 2021-01-25 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0004_answertypeoption_answertypetext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='custom_user',
        ),
    ]
