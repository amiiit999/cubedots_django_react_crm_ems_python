# Generated by Django 3.1.7 on 2021-04-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_cubedots', '0002_auto_20210428_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='parent_id',
            field=models.BigIntegerField(default=0),
        ),
    ]