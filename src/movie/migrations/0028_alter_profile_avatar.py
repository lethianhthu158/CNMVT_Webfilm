# Generated by Django 3.2.15 on 2022-11-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0027_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='user_profile/anonymous.PNG', null=True, upload_to='user_profile'),
        ),
    ]
