# Generated by Django 2.2.3 on 2019-07-21 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20190722_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
    ]