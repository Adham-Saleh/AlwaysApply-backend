# Generated by Django 5.1.4 on 2024-12-15 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=255)),
                ('verified', models.BooleanField(default=False)),
                ('certification', models.DateField(blank=True, null=True)),
                ('plans', models.CharField(choices=[('standard', 'standard'), ('premium', 'premium')], default='standard', max_length=25)),
                ('rates', models.DecimalField(decimal_places=2, default=5.0, max_digits=5)),
                ('connects', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('connects', models.IntegerField(default=10)),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('budget', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('renewed_at', models.DateTimeField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('connects_required', models.IntegerField(default=10)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='employer.employer')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isAccepted', models.BooleanField(default=False)),
                ('isPending', models.BooleanField(default=True)),
                ('connects', models.IntegerField()),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('rejection_reason', models.TextField(blank=True, null=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='employer.freelancer')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='employer.job')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDone', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='employer.job')),
            ],
        ),
    ]
