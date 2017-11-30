# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PacketM',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('proto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ArpM',
            fields=[
                ('packet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wshark.PacketM')),
                ('hardware_type', models.CharField(max_length=50)),
                ('protocol_type', models.CharField(max_length=50)),
                ('hardware_size', models.CharField(max_length=50)),
                ('protocol_size', models.CharField(max_length=50)),
                ('opcode', models.CharField(max_length=50)),
                ('sender_mac_address', models.CharField(max_length=50)),
                ('sender_ip_address', models.CharField(max_length=50)),
                ('target_mac_address', models.CharField(max_length=50)),
                ('target_ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EtherM',
            fields=[
                ('packet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wshark.PacketM')),
                ('d_mac', models.CharField(max_length=50)),
                ('s_mac', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('next_proto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IcmpM',
            fields=[
                ('packet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wshark.PacketM')),
            ],
        ),
        migrations.CreateModel(
            name='IpM',
            fields=[
                ('packet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wshark.PacketM')),
                ('version', models.CharField(max_length=50)),
                ('header_length', models.CharField(max_length=50)),
                ('dsf', models.CharField(max_length=50)),
                ('total_length', models.CharField(max_length=50)),
                ('indentification', models.CharField(max_length=50)),
                ('flags', models.CharField(max_length=50)),
                ('fragment_offset', models.CharField(max_length=50)),
                ('time_to_live', models.CharField(max_length=50)),
                ('next_proto', models.CharField(max_length=50)),
                ('checksum', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TcpM',
            fields=[
                ('packet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wshark.PacketM')),
                ('source_port', models.IntegerField()),
                ('destination_port', models.IntegerField()),
                ('sequence_number', models.BigIntegerField()),
                ('acknowledgement_number', models.BigIntegerField()),
                ('header_length', models.IntegerField()),
                ('syn', models.CharField(max_length=50)),
                ('ack', models.CharField(max_length=50)),
                ('push', models.CharField(max_length=50)),
                ('fin', models.CharField(max_length=50)),
                ('window_size_value', models.IntegerField()),
                ('checksum', models.CharField(max_length=50)),
                ('urgent_pointer', models.CharField(max_length=50)),
                ('options', models.TextField()),
                ('segment_data_length', models.IntegerField()),
                ('actual_data', models.TextField(blank=True, default='', null=True)),
                ('next_proto', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('stream_index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UdpM',
            fields=[
                ('packet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wshark.PacketM')),
            ],
        ),
    ]
