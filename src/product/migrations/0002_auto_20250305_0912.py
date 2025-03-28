# Generated by Django 3.1.4 on 2025-03-05 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_auto_20250305_0912'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('configure', '0002_auto_20250305_0912'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantitywiseproductvariantprice',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_quantitywiseproductvariantprices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quantitywiseproductvariantprice',
            name='product_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='quantitywiseproductvariantprice',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_quantitywiseproductvariantprices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productvariantreview',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_productvariantreviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productvariantreview',
            name='product_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='productvariantreview',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_productvariantreviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productvariantattribute',
            name='attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.attribute'),
        ),
        migrations.AddField(
            model_name='productvariantattribute',
            name='attribute_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.attributevalue'),
        ),
        migrations.AddField(
            model_name='productvariantattribute',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_productvariantattributes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productvariantattribute',
            name='product_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='productvariantattribute',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_productvariantattributes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.brand'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_productvariants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.subcategory'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productunit'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_productvariants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productunit',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_productunits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productunit',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_productunits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='countrywiseproductvariant',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configure.country'),
        ),
        migrations.AddField(
            model_name='countrywiseproductvariant',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_countrywiseproductvariants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='countrywiseproductvariant',
            name='product_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='countrywiseproductvariant',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_countrywiseproductvariants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='productvariantattribute',
            index=models.Index(fields=['-created_at'], name='product_vai_created_38140f_idx'),
        ),
    ]
