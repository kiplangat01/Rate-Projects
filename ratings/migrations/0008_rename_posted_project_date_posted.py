# Generated by Django 4.0.5 on 2022-06-17 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0007_alter_project_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='posted',
            new_name='date_posted',
        ),
    ]
