# Generated by Django 4.0.6 on 2023-05-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0021_alter_coursereg_cupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereg',
            name='cupload',
            field=models.FileField(null=True, upload_to='cupload'),
        ),
    ]
