# Generated by Django 3.1.3 on 2020-11-28 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201129_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
