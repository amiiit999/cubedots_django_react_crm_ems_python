# Generated by Django 3.2.5 on 2021-09-24 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_cubedots', '0028_auto_20210924_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='teamleader',
            name='deleted_at',
        ),
    ]
