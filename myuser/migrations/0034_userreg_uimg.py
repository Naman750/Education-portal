# Generated by Django 4.0.6 on 2023-05-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0033_alter_coursereg_cimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='uimg',
            field=models.ImageField(null=True, upload_to='uimg/'),
        ),
    ]