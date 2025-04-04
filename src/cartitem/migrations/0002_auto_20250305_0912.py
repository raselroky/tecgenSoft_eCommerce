# Generated by Django 3.1.4 on 2025-03-05 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('cartitem', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_cartitems', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_cartitems', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='cartitem',
            index=models.Index(fields=['-created_at'], name='cart_item_created_cb158a_idx'),
        ),
    ]
