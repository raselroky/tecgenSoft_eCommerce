# Generated by Django 3.1.4 on 2024-10-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartitem', '0004_alter_cartitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]