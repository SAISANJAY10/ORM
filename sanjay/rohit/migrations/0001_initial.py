# Generated by Django 5.0.2 on 2024-02-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('dateofpublication', models.DateField()),
                ('genre', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
