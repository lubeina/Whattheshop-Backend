# Generated by Django 2.2.7 on 2020-03-12 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cart_cart_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_total',
        ),
    ]