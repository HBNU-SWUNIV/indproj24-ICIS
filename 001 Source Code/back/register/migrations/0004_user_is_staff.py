# Generated by Django 5.1 on 2024-09-03 01:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("register", "0003_remove_user_is_admin_remove_user_is_staff_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]
