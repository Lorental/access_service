# Generated by Django 4.2.13 on 2024-08-28 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access_engine', '0015_alter_employee_company_alter_itasset_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techaccount',
            name='role',
        ),
    ]
