# Generated by Django 2.2.6 on 2020-02-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='github_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
