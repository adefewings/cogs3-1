# Generated by Django 2.0.2 on 2018-03-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]