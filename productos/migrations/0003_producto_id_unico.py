# Generated by Django 5.1.3 on 2024-12-05 03:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_descripcion_alter_producto_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id_unico',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
