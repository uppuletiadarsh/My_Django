# Generated by Django 5.1 on 2024-09-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Empid', models.IntegerField(primary_key=True, serialize=False)),
                ('Domain', models.CharField(max_length=20)),
            ],
        ),
    ]
