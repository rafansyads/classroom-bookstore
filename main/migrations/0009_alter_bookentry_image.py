# Generated by Django 5.1.1 on 2024-09-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_bookentry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/'),
        ),
    ]
