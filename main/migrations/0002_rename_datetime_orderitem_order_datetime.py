# Generated by Django 5.1.2 on 2024-10-30 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='datetime',
            new_name='order_datetime',
        ),
    ]
