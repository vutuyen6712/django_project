# Generated by Django 2.2.4 on 2019-09-12 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parentID',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]