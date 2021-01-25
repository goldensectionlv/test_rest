# Generated by Django 2.2.1 on 2021-01-25 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0009_answeroption_poll'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.CharField(blank=True, max_length=1024, null=True)),
                ('AnswerBoolean', models.BooleanField()),
                ('custom_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='poll2.CustomUser')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll2.Poll')),
                ('question', models.ManyToManyField(blank=True, related_name='user_question_rel', to='poll2.Question')),
            ],
        ),
    ]