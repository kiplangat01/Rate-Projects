# Generated by Django 4.0.5 on 2022-06-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=1200, verbose_name='Description'),
        ),
    ]
