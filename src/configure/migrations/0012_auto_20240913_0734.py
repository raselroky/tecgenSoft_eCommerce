# Generated by Django 3.1.4 on 2024-09-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configure', '0011_alter_allusedcoupon_id_alter_banner_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allusedcoupon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='multipleaddress',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='platformcoupon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
