# Generated by Django 4.0.3 on 2022-04-09 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iconPath', models.CharField(max_length=60)),
                ('heading', models.CharField(max_length=60)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]
