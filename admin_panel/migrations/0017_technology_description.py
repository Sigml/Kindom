# Generated by Django 5.0.7 on 2025-01-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0016_technology_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
