# Generated by Django 4.2.13 on 2024-07-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0004_course_amount_lesson_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="subscript",
            field=models.BooleanField(default=False, verbose_name="Признак подписки"),
        ),
    ]
