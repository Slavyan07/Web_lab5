# Generated by Django 5.2 on 2025-05-31 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
