# Generated by Django 5.1.4 on 2024-12-13 14:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


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
                ('level', models.CharField(choices=[('ENTRY', 'entry'), ('INTERMEDIATE', 'intermediate'), ('ADVANCED', 'advanced')], default='entry', max_length=200)),
                ('workingMode', models.CharField(choices=[('FULL TIME', 'full'), ('PART TIME', 'part')], default='PART TIME', max_length=200)),
                ('isActive', models.BooleanField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(default=2000.0)),
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
                ('company', models.ForeignKey(default=1, limit_choices_to={'role': 'company'}, on_delete=django.db.models.deletion.CASCADE, related_name='applications_as_company', to=settings.AUTH_USER_MODEL)),
                ('freelancer', models.ForeignKey(limit_choices_to={'role': 'freelancer'}, on_delete=django.db.models.deletion.CASCADE, related_name='applications_as_freelancer', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alwayaApply.job')),
            ],
        ),
    ]
