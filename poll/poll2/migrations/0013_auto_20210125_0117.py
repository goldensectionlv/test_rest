# Generated by Django 2.2.1 on 2021-01-25 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0012_auto_20210125_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='date_ends',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='date_starts',
            field=models.DateField(null=True),
        ),
    ]
