# Generated by Django 5.1.2 on 2024-10-26 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0003_rename_created_at_task_createdat_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="createdAt",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="task",
            old_name="issueAt",
            new_name="issue_at",
        ),
    ]
