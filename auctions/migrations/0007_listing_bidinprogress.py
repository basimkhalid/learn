# Generated by Django 3.1.6 on 2021-02-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_comment_commentdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bidinprogress',
            field=models.BooleanField(default=True),
        ),
    ]
