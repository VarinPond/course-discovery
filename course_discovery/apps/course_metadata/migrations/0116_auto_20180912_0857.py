# Generated by Django 1.11.15 on 2018-09-12 08:57


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0115_increase_read_more_cutoff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
