# Generated by Django 3.2.7 on 2021-11-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_auto_20211102_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
    ]