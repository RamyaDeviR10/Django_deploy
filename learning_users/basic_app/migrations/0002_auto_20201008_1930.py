# Generated by Django 3.1.1 on 2020-10-08 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio',
            new_name='portfolio_site',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='picture',
            new_name='profile_pic',
        ),
    ]
