# Generated by Django 2.2.5 on 2019-09-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190912_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parentID',
            field=models.IntegerField(null=True),
        ),
    ]
