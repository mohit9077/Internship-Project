# Generated by Django 3.0.7 on 2020-07-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200703_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='option_four',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_one',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_three',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='poll',
            name='option_two',
            field=models.CharField(max_length=100),
        ),
    ]
