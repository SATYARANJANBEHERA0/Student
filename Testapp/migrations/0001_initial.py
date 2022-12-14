# Generated by Django 3.2.9 on 2022-08-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lasttname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
                ('Occupation', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Education', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
            ],
        ),
    ]
