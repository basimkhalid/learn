# Generated by Django 3.1.6 on 2021-02-26 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listing_catagory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchuser',
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings_watching', to='auctions.listing')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_watching', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
