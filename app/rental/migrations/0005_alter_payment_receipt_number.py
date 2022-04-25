# Generated by Django 4.0.4 on 2022-04-23 15:49

from django.db import migrations, models
import rental.models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_alter_payment_receipt_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='receipt_number',
            field=models.CharField(default=rental.models.Payment.random_string, editable=False, max_length=50),
        ),
    ]
