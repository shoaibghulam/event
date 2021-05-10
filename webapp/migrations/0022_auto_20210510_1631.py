# Generated by Django 3.1.5 on 2021-05-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_event_buy_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='user_event_registration',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Disable', 'Disable')], default='Disable', max_length=100),
        ),
    ]
