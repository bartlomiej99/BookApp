# Generated by Django 4.0.3 on 2022-04-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_number',
            field=models.BigIntegerField(verbose_name='ISBN number'),
        ),
    ]