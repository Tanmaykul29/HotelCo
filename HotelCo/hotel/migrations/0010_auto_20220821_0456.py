# Generated by Django 3.1 on 2022-08-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_choice_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='start',
        ),
        migrations.AlterField(
            model_name='choice',
            name='checkin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='checkout',
            field=models.DateField(blank=True, null=True),
        ),
    ]
