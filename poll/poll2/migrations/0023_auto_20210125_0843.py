# Generated by Django 2.2.1 on 2021-01-25 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll2', '0022_auto_20210125_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='custom_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll2.CustomUser'),
        ),
    ]
