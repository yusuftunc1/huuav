# Generated by Django 4.1 on 2022-09-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_myappuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myappuser',
            name='grade',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
