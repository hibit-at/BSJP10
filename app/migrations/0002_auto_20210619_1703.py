# Generated by Django 3.1 on 2021-06-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='ssids',
        ),
        migrations.AddField(
            model_name='ranking',
            name='n0',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n2',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n4',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n5',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n6',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n7',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n8',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ranking',
            name='n9',
            field=models.CharField(default='', max_length=50),
        ),
    ]
