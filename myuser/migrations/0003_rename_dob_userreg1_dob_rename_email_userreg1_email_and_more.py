# Generated by Django 4.0.6 on 2023-03-30 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_userreg1_userreg2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreg1',
            old_name='dob',
            new_name='Dob',
        ),
        migrations.RenameField(
            model_name='userreg1',
            old_name='email',
            new_name='Email',
        ),
        migrations.RemoveField(
            model_name='userreg1',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='userreg1',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='userreg2',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='userreg2',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userreg2',
            name='mobile',
        ),
    ]