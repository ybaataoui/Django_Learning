# Generated by Django 4.2.7 on 2023-12-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='reservation_day',
            field=models.CharField(default='Saturday', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='seats',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
