# Generated by Django 4.2.11 on 2024-09-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_auto_20240910_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinepayment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderpaymentmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
