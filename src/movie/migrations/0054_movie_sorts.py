# Generated by Django 3.2.15 on 2022-11-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0053_auto_20221130_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='sorts',
            field=models.CharField(choices=[('Newest', 'Newest'), ('Most view', 'Most view'), ('New Update', 'New Update')], default='Newest', max_length=20),
        ),
    ]
