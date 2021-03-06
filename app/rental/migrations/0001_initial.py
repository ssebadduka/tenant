# Generated by Django 4.0.4 on 2022-04-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_rent_due', models.CharField(max_length=50)),
                ('date_begin', models.DateField(auto_now=True)),
                ('date_end', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contract',
                'verbose_name_plural': 'Contract',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_type', models.CharField(max_length=50)),
                ('number_of_rooms', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Property',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Tenant',
                'verbose_name_plural': 'Tenant',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('Single', 'Single'), ('Double', 'Double')], default='Single', max_length=50)),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_name', to='rental.property')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Room',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paid', models.DateField(auto_now=True)),
                ('amount_paid', models.IntegerField()),
                ('Balance', models.IntegerField()),
                ('payment_status', models.CharField(choices=[('Cleared', 'Cleared'), ('Balance', 'Balance')], default='Cleared', max_length=50)),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_name', to='rental.contract')),
                ('monthly_rent_due', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Due_Rent', to='rental.contract')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant_name', to='rental.tenant')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payment',
            },
        ),
        migrations.AddField(
            model_name='contract',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_name', to='rental.room'),
        ),
        migrations.AddField(
            model_name='contract',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenant_names', to='rental.tenant'),
        ),
    ]
