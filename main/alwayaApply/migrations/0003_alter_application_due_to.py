# Generated by Django 4.2.16 on 2024-12-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alwayaApply', '0002_alter_application_due_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='due_to',
            field=models.DateField(default='18-12-2024'),
        ),
    ]
