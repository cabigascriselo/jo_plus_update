# Generated by Django 5.1.3 on 2024-12-17 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approver', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Issued_To',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jo_issued_to', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Requestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts', models.CharField(max_length=64)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spare_parts', to='job_order.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specs', models.TextField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='job_order.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.CharField(max_length=64)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='job_order.location')),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machines', to='job_order.process'),
        ),
        migrations.CreateModel(
            name='Job_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('complaint', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('lead_times', models.IntegerField(default=0)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approve_by', to='job_order.approver')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='job_order.department')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machine_unit', to='job_order.equipment')),
                ('issued_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='job_order.issued_to')),
                ('parts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts_lists', to='job_order.equipmentparts')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area_located', to='job_order.location')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='systems', to='job_order.process')),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_by', to='job_order.requestor')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_type', to='job_order.service_type')),
            ],
        ),
    ]
