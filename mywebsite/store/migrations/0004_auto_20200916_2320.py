# Generated by Django 3.1 on 2020-09-16 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200916_2318'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Product',
        ),
    ]
