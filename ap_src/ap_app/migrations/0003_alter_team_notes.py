# Generated by Django 3.2.9 on 2022-10-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap_app', '0002_team_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='notes',
            field=models.CharField(default='', max_length=512),
        ),
    ]