# Generated by Django 4.2.11 on 2024-08-09 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category',
        ),
    ]
