# Generated by Django 4.0 on 2022-08-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_announcements_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='postdate',
            field=models.DateField(blank=True, null=True, verbose_name='yayınlanma tarihi'),
        ),
    ]
