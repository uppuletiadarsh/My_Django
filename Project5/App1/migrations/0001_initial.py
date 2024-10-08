# Generated by Django 5.1 on 2024-09-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=20, unique=True)),
                ('physics', models.PositiveIntegerField()),
                ('chemistry', models.PositiveIntegerField()),
                ('english', models.PositiveIntegerField()),
                ('total_marks', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
