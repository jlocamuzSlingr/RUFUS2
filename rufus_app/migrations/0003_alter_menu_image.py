# Generated by Django 4.2 on 2023-05-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rufus_app', '0002_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='', upload_to='staticfiles/rest_framework/img/'),
        ),
    ]