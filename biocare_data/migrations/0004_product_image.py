# Generated by Django 4.2.1 on 2023-07-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biocare_data', '0003_product_pt10_head_product_pt10_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='0', upload_to='product_img'),
            preserve_default=False,
        ),
    ]
