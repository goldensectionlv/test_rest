# Generated by Django 2.2.1 on 2021-01-25 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0018_question_question_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='AnswerBoolean',
            new_name='answer_boolean',
        ),
    ]
