# Generated by Django 3.2.6 on 2021-09-06 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=70)),
                ('marks', models.IntegerField()),
            ],
            options={
                'db_table': 'Students',
            },
        ),
    ]
