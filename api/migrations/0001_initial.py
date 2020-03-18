# Generated by Django 2.2.7 on 2020-03-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('flavor', models.CharField(max_length=250)),
                ('size', models.CharField(max_length=100)),
                ('shape', models.CharField(max_length=100)),
            ],
        ),
    ]
