# Generated by Django 3.1 on 2022-08-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_alllist'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyHotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('roomtype', models.CharField(max_length=64)),
                ('cost', models.IntegerField()),
                ('address', models.CharField(max_length=364)),
            ],
        ),
        migrations.DeleteModel(
            name='AllList',
        ),
    ]
