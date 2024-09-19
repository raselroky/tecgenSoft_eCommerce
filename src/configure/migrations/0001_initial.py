# Generated by Django 3.1.4 on 2024-09-19 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_multipleaddresss', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_multipleaddresss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
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
                ('flag', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_countrys', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_countrys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'country',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images')),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_banners', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_banners', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'banners',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='AllUsedCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_invoice', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['currency_code'], name='country_currenc_8292a3_idx'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['code'], name='country_code_f89761_idx'),
        ),
        migrations.AddIndex(
            model_name='banner',
            index=models.Index(fields=['-created_at'], name='banners_created_995d20_idx'),
        ),
        migrations.AddIndex(
            model_name='banner',
            index=models.Index(fields=['is_active'], name='banners_is_acti_01b940_idx'),
        ),
    ]
