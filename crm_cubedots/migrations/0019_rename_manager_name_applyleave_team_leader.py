# Generated by Django 3.2.5 on 2021-09-22 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_cubedots', '0018_alter_applyleave_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applyleave',
            old_name='manager_name',
            new_name='team_leader',
        ),
    ]