# Generated by Django 2.1.3 on 2018-11-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0010_essay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=2000)),
                ('url', models.URLField(null=True)),
                ('time', models.DateField()),
            ],
        ),
    ]
