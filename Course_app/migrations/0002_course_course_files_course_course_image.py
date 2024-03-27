# Generated by Django 5.0.3 on 2024-03-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_files',
            field=models.FileField(null=True, upload_to='course_materials/'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
