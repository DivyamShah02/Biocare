# Generated by Django 4.2.1 on 2023-07-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biocare_data', '0002_product_pt1_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pt10_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt10_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt1_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt2_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt2_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt3_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt3_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt4_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt4_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt5_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt5_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt6_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt6_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt7_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt7_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt8_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt8_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt9_head',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pt9_value',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]