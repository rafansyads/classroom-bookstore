# Generated by Django 5.1.1 on 2024-09-15 05:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_bookentry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookentry',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]