# Generated by Django 4.0.6 on 2023-03-30 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userReg3',
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