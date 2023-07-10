# Generated by Django 4.2.1 on 2023-07-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biocare_data', '0004_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=255)),
                ('para_1', models.TextField()),
                ('para_2', models.TextField()),
                ('head_image', models.ImageField(upload_to='blog_img')),
                ('secondary_image_1', models.ImageField(upload_to='blog_img')),
                ('secondary_image_2', models.ImageField(upload_to='blog_img')),
                ('views', models.TextField(default=0, max_length=100)),
            ],
        ),
    ]
