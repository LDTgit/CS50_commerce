# Generated by Django 4.1.5 on 2023-02-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_listing_post_date_alter_category_category_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(max_length=64),
        ),
    ]