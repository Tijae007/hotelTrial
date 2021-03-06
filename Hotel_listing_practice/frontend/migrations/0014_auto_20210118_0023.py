# Generated by Django 3.1.1 on 2021-01-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_auto_20210117_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Founder Image'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_name',
            field=models.CharField(default=1, max_length=150, verbose_name='Founder Name'),
            preserve_default=False,
        ),
    ]
