# Generated by Django 3.2.5 on 2021-07-04 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_merge_0002_auto_20210623_0915_0008_auto_20210630_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerregistration',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employerregistration',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='level',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True)),
                ('course', models.CharField(blank=True, max_length=100, null=True)),
                ('school_id', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('twitter_handle', models.CharField(max_length=100)),
                ('linkedin_link', models.CharField(max_length=500)),
                ('student_reg_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.studentregistration')),
            ],
        ),
    ]
