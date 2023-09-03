# Generated by Django 4.2.1 on 2023-09-03 07:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("coala", "0003_performance"),
    ]

    operations = [
        migrations.AddField(
            model_name="performance",
            name="registered_datetime",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="performance",
            name="performance",
            field=models.CharField(max_length=20),
        ),
    ]