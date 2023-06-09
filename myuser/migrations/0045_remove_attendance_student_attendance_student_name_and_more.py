# Generated by Django 4.0.6 on 2023-05-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0044_alter_attendance_is_present'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='is_present',
            field=models.BooleanField(default=True),
        ),
    ]
