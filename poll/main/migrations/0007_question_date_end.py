# Generated by Django 2.2.1 on 2021-01-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_question_date_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date_end',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='end'),
        ),
    ]
