# Generated by Django 3.2.5 on 2021-09-23 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_cubedots', '0021_applyleave_team_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tl_name', models.CharField(max_length=100)),
                ('tl_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='managerId', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'manager',
            },
        ),
    ]
