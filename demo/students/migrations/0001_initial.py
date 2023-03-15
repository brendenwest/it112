# Generated by Django 3.2.13 on 2023-02-15 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('graduation', models.IntegerField(blank=True, null=True)),
                ('year',
                 models.CharField(choices=[('FR', 'Freshman'),
                                           ('SO', 'Sophomore'),
                                           ('JR', 'Junior'), ('SR', 'Senior'),
                                           ('GR', 'Graduate')],
                                  max_length=25)),
            ],
        ),
    ]