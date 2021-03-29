# Generated by Django 2.2 on 2021-03-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksAuthors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('books', models.ManyToManyField(related_name='authors', to='booksAuthors.Book')),
            ],
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]