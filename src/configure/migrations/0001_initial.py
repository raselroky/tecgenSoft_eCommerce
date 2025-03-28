# Generated by Django 3.1.4 on 2025-03-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUsedCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_invoice', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.JSONField(default=list)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('ordering', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'banners',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('currency_code', models.CharField(blank=True, max_length=500, null=True)),
                ('code', models.CharField(blank=True, max_length=500, null=True)),
                ('flag', models.JSONField(default=list)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'country',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MultipleAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('number', models.CharField(blank=True, max_length=14, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlatformCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('promo_code', models.CharField(max_length=1000, null=True, unique=True)),
                ('discount_type', models.CharField(choices=[('select', 'select'), ('flat', 'flat'), ('percentage', 'percentage')], default='select', max_length=1000)),
                ('promo_amount', models.FloatField(default=0)),
                ('active_use_limit', models.BooleanField(default=False)),
                ('use_limit', models.IntegerField(default=0)),
                ('used', models.IntegerField(default=0)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
