# Generated by Django 4.1.5 on 2023-01-20 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_user_file_delete_user_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_file',
            options={'ordering': ('User',)},
        ),
        migrations.RenameField(
            model_name='user_file',
            old_name='username',
            new_name='User',
        ),
    ]
