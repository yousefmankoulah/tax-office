# Generated by Django 4.1.5 on 2023-01-23 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_user_file_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_file',
            options={'ordering': ('user',)},
        ),
        migrations.RenameField(
            model_name='user_file',
            old_name='User',
            new_name='user',
        ),
    ]
