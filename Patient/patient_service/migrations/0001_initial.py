# Generated by Django 4.1.13 on 2024-05-31 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthInsurance',
            fields=[
                ('patient_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('insurance_number', models.CharField(max_length=50, unique=True)),
                ('provider_name', models.CharField(max_length=100)),
                ('policy_start_date', models.DateField()),
                ('policy_end_date', models.DateField()),
                ('coverage_details', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('health_insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_service.healthinsurance')),
            ],
        ),
    ]
