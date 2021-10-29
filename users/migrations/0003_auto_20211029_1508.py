# Generated by Django 3.2.8 on 2021-10-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211029_1034'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='apiuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='apiuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='apiuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]