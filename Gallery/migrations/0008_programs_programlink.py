# Generated by Django 3.2.3 on 2021-06-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0007_auto_20210601_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='ProgramLink',
            field=models.CharField(default='#', max_length=300),
        ),
    ]
