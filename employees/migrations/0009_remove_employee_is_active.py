# Generated by Django 4.2.4 on 2023-09-01 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_alter_employee_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
    ]
