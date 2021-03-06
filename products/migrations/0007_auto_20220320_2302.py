# Generated by Django 3.2 on 2022-03-20 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_productreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(3, '3'), (2, '2'), (1, '1')], default=3),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
