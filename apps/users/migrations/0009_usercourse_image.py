# Generated by Django 2.0.1 on 2018-02-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180126_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='image',
            field=models.ImageField(default='defaultXfull.png', upload_to='make_upload_path'),
        ),
    ]