# Generated by Django 4.2.13 on 2024-08-25 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('access_engine', '0005_alter_log_action_delete_logaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to='access_engine.company', verbose_name='Юр.лицо'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contragent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='access_engine.contragent', verbose_name='Контрагент'),
        ),
    ]
