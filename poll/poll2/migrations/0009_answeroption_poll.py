# Generated by Django 2.2.1 on 2021-01-25 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0008_answeroption_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='answeroption',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poll2.Poll'),
        ),
    ]
