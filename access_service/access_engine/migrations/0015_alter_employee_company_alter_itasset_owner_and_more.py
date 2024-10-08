# Generated by Django 4.2.13 on 2024-08-28 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('access_engine', '0014_alter_contragent_duty_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='access_engine.company', verbose_name='Юр.лицо'),
        ),
        migrations.AlterField(
            model_name='itasset',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itassets', to='access_engine.employee', verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='right',
            name='techaccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rights', to='access_engine.techaccount', verbose_name='Тех.учетка'),
        ),
        migrations.AlterField(
            model_name='techaccount',
            name='itasset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='techaccounts', to='access_engine.itasset', verbose_name='Сервис'),
        ),
        migrations.AlterField(
            model_name='techaccount',
            name='role',
            field=models.ManyToManyField(related_name='techaccounts', to='access_engine.role', verbose_name='Роль / Полномочия'),
        ),
    ]
