# Generated by Django 2.2.10 on 2020-03-13 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0019_auto_20200304_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='hidden',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
