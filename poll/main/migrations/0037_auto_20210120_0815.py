# Generated by Django 2.2.1 on 2021-01-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_answerwithmanychoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_starts',
            field=models.DateField(editable=False, null=True),
        ),
    ]
