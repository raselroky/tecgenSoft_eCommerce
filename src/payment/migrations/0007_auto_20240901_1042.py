# Generated by Django 3.1.4 on 2024-09-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_alter_onlinepayment_id_orderpaymentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinepayment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderpaymentmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
