# Generated by Django 3.1.4 on 2024-10-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_alter_stock_id_alter_stockhistory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
