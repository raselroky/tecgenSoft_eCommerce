# Generated by Django 3.1.4 on 2025-03-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnlinePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction_number', models.SlugField(max_length=200, unique=True)),
                ('payment_method', models.CharField(choices=[('ssl_ecommerce', 'ssl_ecommerce'), ('aamarpay', 'aamarpay')], max_length=15)),
                ('amount', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('valid', 'valid'), ('cancelled', 'cancelled'), ('unattempted', 'unattempted'), ('failed', 'failed'), ('successful', 'successful'), ('expired', 'expired')], max_length=15)),
                ('has_hit_ipn', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'online_payments',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderPaymentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('paid_amount', models.FloatField(default=0)),
                ('payment_method', models.CharField(choices=[('cash_on_delivery', 'cash_on_delivery'), ('cash', 'cash'), ('bank', 'Bank'), ('card', 'card'), ('mobile_bank', 'mobile_bank'), ('online', 'online')], max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
