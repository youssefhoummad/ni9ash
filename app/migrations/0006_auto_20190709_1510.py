# Generated by Django 2.2.2 on 2019-07-09 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='user',
            new_name='created_by',
        ),
    ]
