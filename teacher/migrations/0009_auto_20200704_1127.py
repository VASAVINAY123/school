# Generated by Django 2.2.3 on 2020-07-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_classupload1_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classupload1',
            name='file',
            field=models.FileField(upload_to='files/pdfs/'),
        ),
    ]
