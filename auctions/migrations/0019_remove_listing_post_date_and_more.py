# Generated by Django 4.1.5 on 2023-02-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_listing_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='post_date',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(max_length=64),
        ),
    ]
