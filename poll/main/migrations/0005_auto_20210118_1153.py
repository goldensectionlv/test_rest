# Generated by Django 2.2.1 on 2021-01-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210118_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_end',
            field=models.DateTimeField(verbose_name='end'),
        ),
    ]
