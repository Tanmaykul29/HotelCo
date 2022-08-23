# Generated by Django 3.1 on 2022-08-21 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20220821_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myhotels',
            name='address',
        ),
        migrations.RemoveField(
            model_name='myhotels',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='myhotels',
            name='name',
        ),
        migrations.RemoveField(
            model_name='myhotels',
            name='roomtype',
        ),
        migrations.AddField(
            model_name='myhotels',
            name='hoteladdress',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='myhotels',
            name='hotelname',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='myhotels',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myhotels',
            name='rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myhotels',
            name='type',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
