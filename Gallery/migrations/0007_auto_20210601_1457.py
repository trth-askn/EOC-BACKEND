# Generated by Django 3.2.3 on 2021-06-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0006_alter_programs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.FileField(upload_to='programs/images/'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='image',
            field=models.FileField(blank=True, upload_to='programs/images/'),
        ),
    ]
