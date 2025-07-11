# Generated by Django 3.0.5 on 2020-07-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_fileupload2'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileupload10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload10',
            },
        ),
        migrations.CreateModel(
            name='fileupload11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload11',
            },
        ),
        migrations.CreateModel(
            name='fileupload12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload12',
            },
        ),
        migrations.CreateModel(
            name='fileupload3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload3',
            },
        ),
        migrations.CreateModel(
            name='fileupload4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload4',
            },
        ),
        migrations.CreateModel(
            name='fileupload5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload5',
            },
        ),
        migrations.CreateModel(
            name='fileupload6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload6',
            },
        ),
        migrations.CreateModel(
            name='fileupload7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload7',
            },
        ),
        migrations.CreateModel(
            name='fileupload8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload8',
            },
        ),
        migrations.CreateModel(
            name='fileupload9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'fileupload9',
            },
        ),
    ]
