# Generated by Django 5.1 on 2024-10-01 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_rename_contact_contect_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contect_message',
        ),
    ]
