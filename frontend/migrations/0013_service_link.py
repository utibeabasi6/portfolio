# Generated by Django 3.2.4 on 2021-06-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_remove_service_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
