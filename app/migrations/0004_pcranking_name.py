# Generated by Django 2.2 on 2021-12-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_pcranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcranking',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]