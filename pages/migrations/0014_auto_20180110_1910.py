# Generated by Django 2.0 on 2018-01-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20180110_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='first_cena',
            field=models.IntegerField(default='', verbose_name='Цена без учета скидки'),
        ),
    ]
