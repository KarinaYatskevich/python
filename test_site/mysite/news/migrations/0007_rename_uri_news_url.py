# Generated by Django 3.2.3 on 2021-06-08 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210608_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='URI',
            new_name='URL',
        ),
    ]