# Generated by Django 5.1.2 on 2024-10-26 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="createAt",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="task",
            old_name="issueAt",
            new_name="updated_at",
        ),
    ]
