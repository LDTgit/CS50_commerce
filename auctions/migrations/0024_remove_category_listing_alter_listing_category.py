# Generated by Django 4.1.5 on 2023-02-16 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_category_category_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='listing',
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.category'),
        ),
    ]