# Generated by Django 2.2.1 on 2021-01-25 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0021_question_question_periodic_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('TEXT_ANSWER', 'TEXT_ANSWER'), ('OPTIONS_ANSWER', 'OPTIONS_ANSWER')], default='TEXT_ANSWER', max_length=255),
        ),
    ]
