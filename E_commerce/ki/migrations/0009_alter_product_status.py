# Generated by Django 4.1.1 on 2022-09-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ki", "0008_alter_product_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="status",
            field=models.IntegerField(
                choices=[(0, "normal_product"), (1, "wishlist")], default=0
            ),
        ),
    ]
