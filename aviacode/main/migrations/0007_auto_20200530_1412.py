# Generated by Django 3.0.6 on 2020-05-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_auto_20200530_1333"),
    ]

    operations = [
        migrations.RenameField(
            model_name="inputtype", old_name="_type", new_name="input_type",
        ),
    ]