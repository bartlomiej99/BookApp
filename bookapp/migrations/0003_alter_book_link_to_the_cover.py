# Generated by Django 4.0.3 on 2022-04-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_alter_book_isbn_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='link_to_the_cover',
            field=models.SlugField(max_length=256, verbose_name='Link to the cover'),
        ),
    ]
