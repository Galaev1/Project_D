# Generated by Django 4.2.4 on 2023-09-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_alter_employee_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_employee_active'),
        ),
    ]
