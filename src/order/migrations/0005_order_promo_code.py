# Generated by Django 4.2.11 on 2024-08-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderitem_discount_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
