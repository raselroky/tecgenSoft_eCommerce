# Generated by Django 4.2.11 on 2024-07-25 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=500, unique=True)),
                ('show_in_ecommerce', models.BooleanField(default=False)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('icon', models.FileField(blank=True, null=True, upload_to='iamges')),
                ('logo', models.FileField(blank=True, null=True, upload_to='images')),
                ('is_active', models.BooleanField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to='user.users')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.users')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=500, unique=True)),
                ('show_in_ecommerce', models.BooleanField(default=False)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('icon', models.FileField(blank=True, null=True, upload_to='iamges')),
                ('logo', models.FileField(blank=True, null=True, upload_to='images')),
                ('is_active', models.BooleanField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to='user.users')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.users')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=500, unique=True)),
                ('show_in_ecommerce', models.BooleanField(default=False)),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('icon', models.FileField(blank=True, null=True, upload_to='iamges')),
                ('logo', models.FileField(blank=True, null=True, upload_to='images')),
                ('is_active', models.BooleanField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to='user.users')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.subcategory')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.users')),
            ],
        ),
    ]
