# Generated by Django 4.0.6 on 2023-03-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userReg1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='userReg2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
