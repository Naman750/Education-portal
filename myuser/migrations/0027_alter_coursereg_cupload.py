# Generated by Django 4.0.6 on 2023-05-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0026_coursereg_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereg',
            name='cupload',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
