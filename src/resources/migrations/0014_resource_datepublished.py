# Generated by Django 2.2.10 on 2020-03-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0013_auto_20200303_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='datePublished',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
