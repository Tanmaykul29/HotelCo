# Generated by Django 3.1 on 2022-08-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20220820_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
