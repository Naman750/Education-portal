# Generated by Django 4.0.6 on 2023-04-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0005_rename_cdur_coursereg_batchday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('startdate', models.CharField(max_length=30)),
                ('cbatch', models.CharField(max_length=30)),
                ('batchday', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CourseReg1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30)),
                ('csyll', models.CharField(max_length=100)),
                ('cfee', models.IntegerField()),
                ('cdur', models.CharField(max_length=30)),
            ],
        ),
    ]
