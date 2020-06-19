# Generated by Django 3.0.6 on 2020-06-11 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_category_name'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
    ]