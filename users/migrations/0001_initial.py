# Generated by Django 5.1.7 on 2025-03-31 12:26

import django.core.validators
import django.db.models.deletion
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignerLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('cell', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=30)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('I', 'Intersex')], default='M', max_length=1)),
                ('phone', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number.', regex='^\\+?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(blank=True, default=users.models.get_default_profile_pic, null=True, upload_to='profile_pics/')),
                ('date_of_birth', models.DateField()),
                ('is_foreigner', models.BooleanField(default=False)),
                ('foreign_location', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userlocation')),
            ],
        ),
    ]
