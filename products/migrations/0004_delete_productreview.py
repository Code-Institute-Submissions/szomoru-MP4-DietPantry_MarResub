# Generated by Django 3.2 on 2022-03-08 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productreview_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductReview',
        ),
    ]