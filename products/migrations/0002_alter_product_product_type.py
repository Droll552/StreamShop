# Generated by Django 3.2.4 on 2021-07-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('media', 'Media'), ('cards', 'Cards'), ('gaming', 'Gaming'), ('comics', 'Comics'), ('shoes', 'Shoes')], max_length=6, verbose_name='Product Type'),
        ),
    ]
