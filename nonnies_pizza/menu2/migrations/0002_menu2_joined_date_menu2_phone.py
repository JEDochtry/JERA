# Generated by Django 4.2 on 2023-04-30 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu2',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='menu2',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]