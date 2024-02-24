# Generated by Django 4.0.6 on 2022-07-18 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learner', '0012_remove_course_cresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cresource',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learner.teacher'),
            preserve_default=False,
        ),
    ]
