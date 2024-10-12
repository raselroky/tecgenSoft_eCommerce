# Generated by Django 4.2.11 on 2024-09-26 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('configure', '0002_initial'),
        ('store', '0001_initial'),
        ('stock', '0001_initial'),
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockhistory',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='product_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.stock'),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stock',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configure.country'),
        ),
        migrations.AddField(
            model_name='stock',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stock',
            name='product_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='stock',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
        migrations.AddField(
            model_name='stock',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='stockhistory',
            index=models.Index(fields=['-created_at'], name='stock_histo_created_7eccf5_idx'),
        ),
        migrations.AddIndex(
            model_name='stockhistory',
            index=models.Index(fields=['type'], name='stock_histo_type_ffb87d_idx'),
        ),
        migrations.AddIndex(
            model_name='stockhistory',
            index=models.Index(fields=['invoice_no'], name='stock_histo_invoice_6476e6_idx'),
        ),
        migrations.AddIndex(
            model_name='stock',
            index=models.Index(fields=['-created_at'], name='stocks_created_4b4953_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together={('store', 'product_variant', 'country')},
        ),
    ]
