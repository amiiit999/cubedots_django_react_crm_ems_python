# Generated by Django 3.2.5 on 2021-09-24 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_cubedots', '0031_auto_20210924_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyleave',
            name='tl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ManagerTlId', to=settings.AUTH_USER_MODEL, verbose_name='TL Name'),
        ),
    ]
