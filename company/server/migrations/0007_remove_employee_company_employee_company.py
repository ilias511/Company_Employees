# Generated by Django 4.1.4 on 2022-12-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_alter_employee_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ManyToManyField(to='server.company'),
        ),
    ]