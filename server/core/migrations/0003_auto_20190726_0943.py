# Generated by Django 2.2.3 on 2019-07-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190725_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]