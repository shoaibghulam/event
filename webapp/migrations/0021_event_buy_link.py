# Generated by Django 3.1.5 on 2021-05-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_auto_20210503_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='buy_link',
            field=models.TextField(default=''),
        ),
    ]
