# Generated by Django 4.0.1 on 2022-07-09 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20211015_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='moneda',
            field=models.CharField(default='$CL', max_length=6),
        ),
    ]