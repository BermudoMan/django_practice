# Generated by Django 4.2.9 on 2024-01-19 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]