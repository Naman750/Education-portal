# Generated by Django 4.0.6 on 2023-04-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0011_rename_passw_userreg_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='repw',
            field=models.CharField(default=1.0, max_length=30),
            preserve_default=False,
        ),
    ]
