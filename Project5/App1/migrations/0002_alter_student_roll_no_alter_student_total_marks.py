# Generated by Django 5.1 on 2024-09-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='total_marks',
            field=models.PositiveIntegerField(),
        ),
    ]
