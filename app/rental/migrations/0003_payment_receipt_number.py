# Generated by Django 4.0.4 on 2022-04-23 15:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_alter_contract_date_begin_alter_contract_date_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='receipt_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
