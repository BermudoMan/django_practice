# Generated by Django 4.2.9 on 2024-01-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryitem',
            name='text',
            field=models.TextField(default=1, verbose_name='some_info'),
            preserve_default=False,
        ),
    ]
