# Generated by Django 3.1.1 on 2021-11-17 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20211024_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Phone number'),
        ),
    ]