# Generated by Django 3.1 on 2020-10-26 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201025_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]