# Generated by Django 3.2.5 on 2021-07-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_alter_studentworkpost_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerprofile',
            name='verified',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
