# Generated by Django 5.0.7 on 2025-03-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0024_remove_technology_vailable'),
        ('game', '0003_newworldtechology'),
    ]

    operations = [
        migrations.AddField(
            model_name='newworld',
            name='unlocking_technology',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newworld',
            name='technologies',
            field=models.ManyToManyField(blank=True, related_name='NewWorldTechnology', to='admin_panel.technology'),
        ),
    ]
