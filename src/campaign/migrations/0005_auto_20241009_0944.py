# Generated by Django 3.1.4 on 2024-10-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_alter_campaign_id_alter_campaignmember_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='campaignmember',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dealoftheweek',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
