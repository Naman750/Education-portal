# Generated by Django 4.0.6 on 2023-05-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0023_coursereg_f_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereg',
            name='f_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
