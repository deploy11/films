# Generated by Django 4.1.7 on 2023-04-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('yili', models.CharField(max_length=100)),
                ('davlat', models.CharField(max_length=500)),
                ('davomiyligi', models.CharField(max_length=500)),
                ('vidio', models.CharField(max_length=500)),
                ('discription', models.TextField(blank=True, null=True)),
                ('rasm', models.CharField(max_length=500)),
            ],
        ),
    ]
