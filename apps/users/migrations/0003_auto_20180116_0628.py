# Generated by Django 2.0.1 on 2018-01-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180111_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourse',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'Administrador'), (2, 'Instructor'), (3, 'Estudiante')], default=3),
        ),
    ]