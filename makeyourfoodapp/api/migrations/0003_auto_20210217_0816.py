# Generated by Django 3.1.6 on 2021-02-17 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210217_0457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appmodel',
            old_name='userid',
            new_name='userId',
        ),
    ]