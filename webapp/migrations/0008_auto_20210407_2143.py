# Generated by Django 3.1.5 on 2021-04-07 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_time_progress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='Description',
            new_name='order_id',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='MaxDateForPayment',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='TypeOrder',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='user_event_registration',
            name='Payment_form',
        ),
        migrations.RemoveField(
            model_name='user_event_registration',
            name='Ruc',
        ),
        migrations.RemoveField(
            model_name='user_signup',
            name='Nrocasa',
        ),
        migrations.AddField(
            model_name='transactions',
            name='event_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.event'),
        ),
    ]
