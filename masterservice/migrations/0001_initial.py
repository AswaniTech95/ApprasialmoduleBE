# Generated by Django 3.0.4 on 2022-05-30 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('dept_id', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('short_notation', models.CharField(blank=True, max_length=8, null=True)),
                ('is_sys', models.BooleanField(default=False)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
