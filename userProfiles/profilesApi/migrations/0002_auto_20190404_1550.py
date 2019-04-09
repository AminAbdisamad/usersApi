# Generated by Django 2.1.7 on 2019-04-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilesApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfileManager',
        ),
    ]