# Generated by Django 4.0.6 on 2022-07-22 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('name_ru',), 'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
    ]
