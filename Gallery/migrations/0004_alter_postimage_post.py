# Generated by Django 3.2.3 on 2021-06-01 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0003_auto_20210601_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='Gallery.programs'),
        ),
    ]
