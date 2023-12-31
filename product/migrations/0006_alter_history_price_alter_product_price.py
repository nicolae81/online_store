# Generated by Django 4.2.6 on 2023-10-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_producthistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
