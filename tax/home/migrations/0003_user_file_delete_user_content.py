# Generated by Django 4.1.5 on 2023-01-20 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_user_content_delete_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=300)),
                ('file_upload', models.FileField(upload_to='')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('username',),
            },
        ),
        migrations.DeleteModel(
            name='User_content',
        ),
    ]
