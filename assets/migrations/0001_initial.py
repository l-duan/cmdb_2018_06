# Generated by Django 2.0.5 on 2018-06-13 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='实例ID')),
                ('hostname', models.CharField(max_length=64, unique=True, verbose_name='主机名')),
                ('public_ip', models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='外网IP')),
                ('private_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP')),
                ('vpn_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='VPN')),
                ('os', models.CharField(blank=True, max_length=128, null=True, verbose_name='系统版本')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存')),
                ('disk', models.CharField(blank=True, max_length=256, null=True, verbose_name='硬盘')),
                ('bandwidth', models.IntegerField(blank=True, default='1', null=True, verbose_name='外网带宽')),
                ('status', models.SmallIntegerField(choices=[(0, '在线'), (1, '下线'), (2, '未知'), (3, '故障'), (4, '销毁')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('last_update', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('expire_time', models.DateTimeField(auto_now=True, null=True, verbose_name='过期时间')),
                ('memo', models.CharField(blank=True, max_length=1024, null=True, verbose_name='备注')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='管理员')),
            ],
        ),
        migrations.CreateModel(
            name='CloudManufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='云厂商名称')),
                ('link_man', models.CharField(max_length=64, unique=True, verbose_name='售后联系人')),
                ('telephone', models.CharField(blank=True, max_length=30, null=True, verbose_name='支持电话')),
                ('QQ', models.CharField(blank=True, max_length=30, null=True, verbose_name='售后支持QQ群')),
                ('DING', models.CharField(blank=True, max_length=30, null=True, verbose_name='售后支持DING群')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '云厂商',
                'verbose_name_plural': '云厂商',
            },
        ),
        migrations.CreateModel(
            name='IDCRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='机房名称')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CloudManufacturer', to='assets.CloudManufacturer')),
            ],
            options={
                'verbose_name': '机房',
                'verbose_name_plural': '机房',
            },
        ),
        migrations.AddField(
            model_name='cloudmachine',
            name='platform',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assets.CloudManufacturer', verbose_name='平台'),
        ),
        migrations.AddField(
            model_name='cloudmachine',
            name='region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assets.IDCRegion', verbose_name='区域'),
        ),
    ]