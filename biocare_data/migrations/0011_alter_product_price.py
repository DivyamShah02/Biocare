# Generated by Django 4.2.1 on 2023-07-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biocare_data', '0010_remove_distributor_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=30),
        ),
    ]
