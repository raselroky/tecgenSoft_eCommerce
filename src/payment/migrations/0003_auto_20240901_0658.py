# Generated by Django 3.1.4 on 2024-09-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinepayment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]