# Generated by Django 5.1.1 on 2024-09-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookentry',
            name='publisher',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]