# Generated by Django 3.1 on 2020-09-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200911_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]