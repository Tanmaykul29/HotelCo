# Generated by Django 3.1 on 2022-08-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20220820_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
                ('checkin', models.CharField(max_length=64)),
                ('checkout', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]