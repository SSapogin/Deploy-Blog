# Generated by Django 2.0.4 on 2018-06-12 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annex', '0013_edit_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_materials',
            name='associate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annex.Materials', verbose_name='Материал'),
        ),
    ]