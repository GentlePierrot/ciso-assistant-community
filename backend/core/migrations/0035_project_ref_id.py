# Generated by Django 5.1.1 on 2024-11-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_fix_loaded_libraries_objects_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ref_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='reference id'),
        ),
    ]
