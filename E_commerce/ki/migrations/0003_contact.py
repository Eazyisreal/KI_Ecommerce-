# Generated by Django 4.0.6 on 2022-09-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ki', '0002_alter_profile_user_alter_profile_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]