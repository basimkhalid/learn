# Generated by Django 3.1.6 on 2021-02-23 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210224_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
