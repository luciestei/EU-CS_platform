# Generated by Django 2.2.10 on 2020-02-25 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20200225_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='uvote',
        ),
        migrations.AddField(
            model_name='votes',
            name='project',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
            preserve_default=False,
        ),
    ]
