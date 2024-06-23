# Generated by Django 4.2 on 2024-06-23 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('users', '0002_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Оплаченный курс'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='Оплаченный урок'),
        ),
    ]
