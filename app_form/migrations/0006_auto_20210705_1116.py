# Generated by Django 3.2.5 on 2021-07-05 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0005_alter_interviewform_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewform',
            name='age',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='interviewform',
            name='candidate_cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='interviewform',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='interviewform',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='interviewform',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='interviewform',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='interviewform',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
