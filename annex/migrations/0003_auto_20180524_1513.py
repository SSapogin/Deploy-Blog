# Generated by Django 2.0.4 on 2018-05-24 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annex', '0002_auto_20180523_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=180, verbose_name='Наименование спецификации проекта')),
                ('etash', models.CharField(default='', max_length=2, verbose_name='Этаж')),
                ('date_push', models.DateTimeField(verbose_name='Дата публикации')),
                ('associate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annex.Company', verbose_name='Компания')),
                ('factory_associate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annex.Factory', verbose_name='Завод')),
            ],
            options={
                'verbose_name': 'Заявки на изготовление',
                'verbose_name_plural': 'Заявки на изготовление',
            },
        ),
        migrations.AlterModelOptions(
            name='materials',
            options={'verbose_name': 'Данные по спецификации', 'verbose_name_plural': 'Данные по спецификации'},
        ),
        migrations.RemoveField(
            model_name='materials',
            name='associate',
        ),
        migrations.RemoveField(
            model_name='materials',
            name='composition',
        ),
        migrations.RemoveField(
            model_name='materials',
            name='factory_associate',
        ),
        migrations.RemoveField(
            model_name='materials',
            name='name',
        ),
        migrations.RemoveField(
            model_name='materials',
            name='price',
        ),
        migrations.RemoveField(
            model_name='materials',
            name='unit',
        ),
        migrations.AddField(
            model_name='materials',
            name='count',
            field=models.CharField(default='', max_length=10, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='materials',
            name='height',
            field=models.CharField(default='', max_length=10, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='materials',
            name='markirovka',
            field=models.CharField(default='', max_length=180, verbose_name='Маркировка изделия'),
        ),
        migrations.AddField(
            model_name='materials',
            name='weight',
            field=models.CharField(default='', max_length=10, verbose_name='Площадь штукатурки,м2'),
        ),
        migrations.AddField(
            model_name='materials',
            name='width',
            field=models.CharField(default='', max_length=10, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('M', 'Менеджер'), ('L', 'Логист'), ('Z', 'Завод'), ('P', 'Директор - партнер'), ('D', 'Директор')], default='Логист', max_length=1, verbose_name='Роль'),
        ),
        migrations.AddField(
            model_name='materials',
            name='specification',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='annex.Specification', verbose_name='Спецификация'),
            preserve_default=False,
        ),
    ]
