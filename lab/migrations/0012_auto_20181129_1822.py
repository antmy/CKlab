# Generated by Django 2.1.3 on 2018-11-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0011_material'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LabNew',
        ),
        migrations.DeleteModel(
            name='TeachWork',
        ),
        migrations.AddField(
            model_name='lecture',
            name='people',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='place',
            field=models.CharField(max_length=100, null=True),
        ),
    ]