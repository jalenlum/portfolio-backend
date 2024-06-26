# Generated by Django 4.2.8 on 2024-04-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_project_description_or_role_project_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='period',
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.CharField(default='', help_text='Enter the the start and end date (present if in progress).', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_or_role',
            field=models.CharField(default='', help_text='Enter the description of the project or your role in the organization.', max_length=100),
        ),
    ]
