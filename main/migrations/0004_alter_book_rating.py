# Generated by Django 5.1.3 on 2024-12-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
