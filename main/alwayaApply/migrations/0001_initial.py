# Generated by Django 4.2.17 on 2024-12-08 21:44

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
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('level', models.CharField(choices=[('entry', 'ENTRY'), ('intermediate', 'INTERMEDIATE'), ('advanced', 'ADVANCED')], default='entry', max_length=200)),
                ('workingMode', models.CharField(choices=[('full', 'FULL TIME'), ('part', 'PART TIME')], default='part', max_length=200)),
                ('isActive', models.BooleanField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(limit_choices_to={'role': 'company'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal', models.TextField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('accepted', 'ACCEPTED'), ('rejected', 'REJECTED')], default='pending', max_length=200)),
                ('duration', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(limit_choices_to={'role': 'company'}, on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL)),
                ('freelancer', models.ForeignKey(limit_choices_to={'role': 'freelancer'}, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alwayaApply.job')),
            ],
        ),
    ]