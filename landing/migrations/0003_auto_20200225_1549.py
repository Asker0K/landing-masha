# Generated by Django 2.2.10 on 2020-02-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20200225_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo',
        ),
        migrations.AlterField(
            model_name='photo',
            name='jpg',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/photos/'),
        ),
    ]
