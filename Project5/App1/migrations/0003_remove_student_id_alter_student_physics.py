# Generated by Django 5.1 on 2024-09-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_alter_student_roll_no_alter_student_total_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='physics',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
