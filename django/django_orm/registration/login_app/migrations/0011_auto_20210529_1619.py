# Generated by Django 3.2.3 on 2021-05-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0010_alter_users_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='user',
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
    ]
