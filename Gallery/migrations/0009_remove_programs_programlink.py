# Generated by Django 3.2.3 on 2021-06-03 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0008_programs_programlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programs',
            name='ProgramLink',
        ),
    ]
