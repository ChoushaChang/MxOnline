# Generated by Django 2.2 on 2019-10-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0014_courseorg_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='click_nums',
            field=models.BigIntegerField(default=0, verbose_name='點擊數'),
        ),
    ]
