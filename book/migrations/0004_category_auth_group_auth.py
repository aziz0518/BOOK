# Generated by Django 5.0.7 on 2024-07-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_product_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='auth',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='auth',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
