# Generated by Django 3.0.6 on 2020-06-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
