# Generated by Django 4.0.6 on 2022-07-18 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0013_course_cresource_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='edc',
            field=models.ManyToManyField(blank=True, default='', to='learner.course'),
        ),
    ]
