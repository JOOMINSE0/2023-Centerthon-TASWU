# Generated by Django 3.2.10 on 2023-08-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20230812_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='coins',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
