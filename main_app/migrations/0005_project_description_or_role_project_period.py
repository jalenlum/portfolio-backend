# Generated by Django 4.2.8 on 2024-04-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_project_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_or_role',
            field=models.CharField(default='', help_text='Enter the technical skills used.', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='period',
            field=models.CharField(default='', help_text='Enter the technical skills used.', max_length=100),
        ),
    ]
