# Generated by Django 3.1.5 on 2021-02-05 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]