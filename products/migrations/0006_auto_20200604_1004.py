# Generated by Django 3.0.6 on 2020-06-04 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200604_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=40),
        ),
    ]
