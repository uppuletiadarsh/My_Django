# Generated by Django 5.1 on 2024-08-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('eid', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=20)),
                ('domain', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
            ],
        ),
    ]
