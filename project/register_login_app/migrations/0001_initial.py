# Generated by Django 4.0.3 on 2022-03-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=50)),
                ('confirmPassword', models.CharField(max_length=50)),
            ],
        ),
    ]
