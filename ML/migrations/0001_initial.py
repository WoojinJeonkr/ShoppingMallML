# Generated by Django 3.2.13 on 2022-05-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week1', models.IntegerField(verbose_name=100)),
                ('week2', models.IntegerField(verbose_name=100)),
                ('hour', models.IntegerField(verbose_name=100)),
                ('gender', models.IntegerField(verbose_name=100)),
                ('age', models.IntegerField(verbose_name=100)),
                ('size', models.IntegerField(verbose_name=10000)),
                ('tag_click', models.IntegerField(verbose_name=300)),
            ],
        ),
    ]
