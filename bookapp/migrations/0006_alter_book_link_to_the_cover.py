# Generated by Django 4.0.3 on 2022-04-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_alter_book_link_to_the_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='link_to_the_cover',
            field=models.URLField(verbose_name='Link to the cover'),
        ),
    ]