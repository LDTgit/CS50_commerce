# Generated by Django 4.1.5 on 2023-02-08 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Biddings',
            new_name='Bidding',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Listings',
            new_name='Listing',
        ),
    ]
