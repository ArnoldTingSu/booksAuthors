# Generated by Django 2.2 on 2021-03-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksAuthors', '0002_auto_20210327_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
