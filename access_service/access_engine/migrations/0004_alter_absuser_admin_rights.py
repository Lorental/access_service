# Generated by Django 4.2.13 on 2024-08-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access_engine', '0003_absuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absuser',
            name='admin_rights',
            field=models.IntegerField(default=1),
        ),
    ]
