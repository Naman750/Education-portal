# Generated by Django 4.0.6 on 2023-04-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0014_alter_userreg_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursereg',
            name='uid',
            field=models.IntegerField(default=1.0),
            preserve_default=False,
        ),
    ]
