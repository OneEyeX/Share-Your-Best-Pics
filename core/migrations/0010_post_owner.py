# Generated by Django 4.0.5 on 2022-06-24 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
            preserve_default=False,
        ),
    ]