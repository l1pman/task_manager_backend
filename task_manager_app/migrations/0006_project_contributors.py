# Generated by Django 4.2 on 2023-04-22 09:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_manager_app', '0005_rename_column_task_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contributors',
            field=models.ManyToManyField(blank=True, related_name='contributors', to=settings.AUTH_USER_MODEL),
        ),
    ]