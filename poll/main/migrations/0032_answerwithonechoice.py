# Generated by Django 2.2.1 on 2021-01-19 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_delete_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerWithOneChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(null=True)),
                ('poll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice_answer_poll_rel', to='main.Poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='one_option_answer', to='main.Question')),
                ('user_poll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_poll_choice_rel', to='main.UserPoll')),
            ],
        ),
    ]
