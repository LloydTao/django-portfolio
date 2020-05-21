# Generated by Django 3.0.5 on 2020-05-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('icon', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=128)),
            ],
        ),
    ]
