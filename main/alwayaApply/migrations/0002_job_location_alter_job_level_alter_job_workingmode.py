# Generated by Django 5.1.4 on 2024-12-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alwayaApply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='EGYPT', max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='level',
            field=models.CharField(choices=[('ENTRY', 'ENTRY'), ('INTERMEDIATE', 'INTERMEDIATE'), ('ADVANCED', 'ADVANCED')], default='ENTRY', max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='workingMode',
            field=models.CharField(choices=[('FULL TIME', 'FULL TIME'), ('PART TIME', 'PART TIME')], default='PART TIME', max_length=200),
        ),
    ]
