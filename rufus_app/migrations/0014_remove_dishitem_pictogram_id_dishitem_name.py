# Generated by Django 4.2 on 2023-05-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rufus_app", "0013_remove_dishitem_name_dish_platos"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dishitem",
            name="pictogram_id",
        ),
        migrations.AddField(
            model_name="dishitem",
            name="name",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
