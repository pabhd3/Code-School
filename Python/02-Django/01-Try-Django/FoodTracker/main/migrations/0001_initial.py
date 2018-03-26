# Generated by Django 2.0.3 on 2018-03-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('flavors', models.CharField(max_length=75)),
                ('num_franchises', models.IntegerField()),
                ('image', models.CharField(max_length=75)),
            ],
        ),
    ]