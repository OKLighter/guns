# Generated by Django 4.2.1 on 2023-05-05 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pistol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=21)),
                ('model', models.CharField(max_length=21)),
                ('author', models.CharField(max_length=21)),
                ('calibre', models.CharField(max_length=21)),
                ('country', models.CharField(max_length=21)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]
