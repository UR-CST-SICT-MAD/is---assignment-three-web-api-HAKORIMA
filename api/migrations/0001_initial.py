# Generated by Django 3.2.9 on 2021-12-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('owner', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('image1', models.CharField(blank=True, max_length=255, null=True)),
                ('image2', models.CharField(blank=True, max_length=255, null=True)),
                ('image3', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
