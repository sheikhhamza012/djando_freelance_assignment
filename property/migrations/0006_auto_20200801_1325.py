# Generated by Django 3.0.8 on 2020-08-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20200801_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='property',
            name='reason',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=10000),
        ),
    ]
