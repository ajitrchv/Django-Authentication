# Generated by Django 4.1 on 2022-09-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
    ]
