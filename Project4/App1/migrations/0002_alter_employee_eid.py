# Generated by Django 5.1 on 2024-08-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
