# Generated by Django 4.0.6 on 2023-05-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0019_coursereg_cprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursereg',
            name='cprice',
            field=models.IntegerField(),
        ),
    ]
