# Generated by Django 3.0.6 on 2020-07-05 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20200705_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
