# Generated by Django 2.2.1 on 2021-01-25 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0002_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_type', models.CharField(choices=[('TEXT_ANSWER', 'TEXT_ANSWER'), ('ONE_OPTION_ANSWER', 'ONE_OPTION_ANSWER'), ('MANY_OPTIONS_ANSWER', 'MANY_OPTIONS_ANSWER')], default='TEXT_ANSWER', max_length=255)),
                ('custom_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll2.CustomUser')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll2.Poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll2.Question')),
            ],
        ),
    ]
