# Generated by Django 5.1 on 2024-09-10 08:36

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
                ('name', models.CharField(max_length=40)),
                ('domain', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=40)),
            ],
        ),
    ]
