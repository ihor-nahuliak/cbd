# Generated by Django 3.1 on 2020-08-21 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MLCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_model_json', models.TextField(blank=True)),
                ('topic_model_cyberbullying_json', models.TextField(blank=True)),
                ('affective_counts_json', models.TextField(blank=True)),
                ('affective_counts_cyberbullying_json', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessedSocialMediaMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('username', models.TextField(blank=True)),
                ('location', models.TextField(blank=True)),
                ('has_bullying', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('Viewer', 'Viewer'), ('Moderatior', 'Moderatior')], default='Viewer', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IncorrectClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cbd.processedsocialmediamessage')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]