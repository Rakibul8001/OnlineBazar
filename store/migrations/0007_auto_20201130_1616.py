# Generated by Django 3.0 on 2020-11-30 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
