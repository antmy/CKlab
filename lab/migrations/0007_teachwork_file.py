# Generated by Django 2.1.3 on 2018-11-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_fun'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachwork',
            name='file',
            field=models.FileField(null=True, upload_to='file'),
        ),
    ]