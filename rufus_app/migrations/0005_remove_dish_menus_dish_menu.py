# Generated by Django 4.2 on 2023-05-04 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rufus_app', '0004_alter_dishitem_name_alter_dishitem_pictogram_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='menus',
        ),
        migrations.AddField(
            model_name='dish',
            name='menu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='rufus_app.menu'),
        ),
    ]
