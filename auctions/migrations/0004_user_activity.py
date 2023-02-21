# Generated by Django 4.1.5 on 2023-01-31 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listings_current_price_alter_listings_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bid', models.IntegerField()),
                ('current_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_listing', to='auctions.listings')),
                ('current_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]