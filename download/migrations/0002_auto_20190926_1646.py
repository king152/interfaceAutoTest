# Generated by Django 2.2.4 on 2019-09-26 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='downloadAuthorTypeName',
            new_name='routeType',
        ),
    ]
