# Generated by Django 5.0.1 on 2024-03-01 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_alter_product_cat_alter_product_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='path',
            field=models.ImageField(default=1, upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Mobile'), (2, 'Shoes'), (3, 'Cloths')], verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
    ]
