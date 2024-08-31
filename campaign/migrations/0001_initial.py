# Generated by Django 4.2.11 on 2024-08-02 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('discount_type', models.CharField(choices=[('flat', 'flat'), ('percentage', 'percentage')], max_length=20)),
                ('min_discount', models.FloatField(default=0)),
                ('max_discount', models.FloatField(default=0)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('image', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('terms_and_conditions', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'campaigns',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CampaignMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discount_type', models.CharField(choices=[('flat', 'flat'), ('percentage', 'percentage')], max_length=10)),
                ('discount_value', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'campaign_members',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DealOfTheWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discount_type', models.CharField(choices=[('flat', 'flat'), ('percentage', 'percentage')], max_length=12)),
                ('discount_value', models.FloatField(default=0)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'deal_of_the_weeks',
                'ordering': ['-created_at'],
            },
        ),
    ]
