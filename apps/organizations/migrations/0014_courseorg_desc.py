# Generated by Django 2.2 on 2019-10-19 00:40

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0013_auto_20191019_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='機構描述'),
        ),
    ]
