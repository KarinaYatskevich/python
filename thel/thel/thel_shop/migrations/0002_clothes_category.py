# Generated by Django 3.2.5 on 2021-07-05 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thel_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='thel_shop.category'),
            preserve_default=False,
        ),
    ]