# Generated by Django 2.0.10 on 2019-01-25 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20190126_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='item_price',
        ),
    ]
