# Generated by Django 2.0.1 on 2018-01-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_usercourse_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourse',
            name='password',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]