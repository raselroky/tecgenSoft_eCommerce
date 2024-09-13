# Generated by Django 3.1.4 on 2024-09-13 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0020_delete_cartitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_cartitems', to=settings.AUTH_USER_MODEL)),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productvariant')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_cartitems', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cart_item',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='cartitem',
            index=models.Index(fields=['-created_at'], name='cart_item_created_cb158a_idx'),
        ),
    ]
