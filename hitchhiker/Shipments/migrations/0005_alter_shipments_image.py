# Generated by Django 5.1 on 2024-09-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shipments', '0004_alter_shipments_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipments',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
