# Generated by Django 4.2 on 2023-05-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("talent", "0005_alter_product_thumbnail_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="thumbnail_image",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]