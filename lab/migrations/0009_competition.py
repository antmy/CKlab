# Generated by Django 2.1.3 on 2018-11-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_auto_20181105_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=2000)),
                ('time', models.DateField()),
            ],
        ),
    ]