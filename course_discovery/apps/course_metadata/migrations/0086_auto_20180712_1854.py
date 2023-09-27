# Generated by Django 1.11.11 on 2018-07-12 18:54


import uuid

import django.db.models.deletion
from django.db import migrations, models

import django_extensions.db.fields  # isort:skip


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0085_creditpathway'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
                'ordering': ('-modified', '-created'),
            },
        ),
        migrations.CreateModel(
            name='DegreeMarketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('application_deadline', models.CharField(help_text='String-based deadline field (e.g. FALL 2020)', max_length=255, unique=True)),
                ('apply_url', models.CharField(blank=True, help_text='Callback URL to partner application flow', max_length=255)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
                'ordering': ('-modified', '-created'),
            },
        ),
        migrations.AddField(
            model_name='degree',
            name='program',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course_metadata.Program'),
        ),
        migrations.AddField(
            model_name='degreemarketing',
            name='degree',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course_metadata.Degree'),
        )
    ]
