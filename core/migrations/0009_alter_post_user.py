# Generated by Django 4.0.5 on 2022-06-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
