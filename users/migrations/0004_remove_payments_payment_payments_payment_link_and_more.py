# Generated by Django 4.2.13 on 2024-07-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_payments_course_alter_payments_lesson"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payments",
            name="payment",
        ),
        migrations.AddField(
            model_name="payments",
            name="payment_link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="id сессии"
            ),
        ),
        migrations.AlterField(
            model_name="payments",
            name="payment_method",
            field=models.CharField(
                default="card", max_length=150, verbose_name="Способ оплаты"
            ),
        ),
    ]
