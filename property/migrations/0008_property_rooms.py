# Generated by Django 3.0.8 on 2020-08-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20200801_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rooms',
            field=models.IntegerField(default=0),
        ),
    ]
