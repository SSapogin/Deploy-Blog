# Generated by Django 2.0 on 2018-01-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20180110_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='first_cena',
            field=models.IntegerField(blank=True, default='', verbose_name='Цена без учета скидки'),
        ),
    ]