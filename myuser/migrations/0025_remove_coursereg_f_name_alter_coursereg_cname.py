# Generated by Django 4.0.6 on 2023-05-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0024_alter_coursereg_f_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursereg',
            name='f_name',
        ),
        migrations.AlterField(
            model_name='coursereg',
            name='cname',
            field=models.TextField(),
        ),
    ]
