# Generated by Django 3.2.8 on 2021-11-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo/%Y%m%d')),
                ('created', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_image',
            },
        ),
    ]