# Generated by Django 4.2.9 on 2024-01-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryitem',
            name='way',
        ),
        migrations.AddField(
            model_name='galleryitem',
            name='file',
            field=models.FileField(default=1, upload_to='main/static/main/'),
            preserve_default=False,
        ),
    ]