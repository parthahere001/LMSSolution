# Generated by Django 4.0.6 on 2022-07-18 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0011_remove_course_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='cresource',
        ),
    ]
