# Generated by Django 4.0.6 on 2023-05-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0034_userreg_uimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursereg',
            name='video_url',
            field=models.URLField(null=True),
        ),
    ]