# Generated by Django 3.0.7 on 2022-12-07 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0012_auto_20221207_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classtudentassignmentsupload',
            name='subject_id',
        ),
    ]
