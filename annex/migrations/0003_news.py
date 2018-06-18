# Generated by Django 2.0.6 on 2018-06-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annex', '0002_auto_20180617_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80, verbose_name='Наименование курса')),
                ('description', models.TextField(verbose_name='Описание')),
                ('background', models.ImageField(default='', upload_to='annex/img/%Y/%m/%d', verbose_name='Фон')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]