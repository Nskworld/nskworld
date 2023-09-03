# Generated by Django 4.2.1 on 2023-09-03 06:28

from django.db import migrations, models


def add_initial_performances(apps, schema_editor):
    Performance = apps.get_model('coala', 'Performance')
    Performance.objects.create(performance='bad')
    Performance.objects.create(performance='not so good')
    Performance.objects.create(performance='so-so')
    Performance.objects.create(performance='good')
    Performance.objects.create(performance='awesome')


class Migration(migrations.Migration):
    initial = True
    
    dependencies = [
        ("coala", "0002_alter_record_time_falling_asleep_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Performance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("performance", models.CharField(max_length=50)),
            ],
        ),
        migrations.RunPython(add_initial_performances)
    ]
