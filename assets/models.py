from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class CloudManufacturer(models.Model):
    """云厂商"""

    name = models.CharField('云厂商名称', max_length=64, unique=True)
    link_man = models.CharField('售后联系人', max_length=64, unique=True)
    telephone = models.CharField('支持电话', max_length=30, blank=True, null=True)
    QQ = models.CharField('售后支持QQ群', max_length=30, blank=True, null=True)
    DING = models.CharField('售后支持DING群', max_length=30, blank=True, null=True)
    memo = models.CharField('备注', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '云厂商'
        verbose_name_plural = "云厂商"


class IDCRegion(models.Model):
    """机房"""
    name = models.CharField(max_length=64, unique=True, verbose_name="机房名称")
    owner = models.ForeignKey(CloudManufacturer, on_delete=models.CASCADE, related_name='CloudManufacturer')
    memo = models.CharField(max_length=128, blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = "机房"


class CloudMachine(models.Model):

    machine_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '销毁'),
    )

    instance_id = models.CharField(max_length=64, verbose_name='实例ID', null=True, blank=True)
    hostname = models.CharField(max_length=64, verbose_name='主机名', unique=True)
    public_ip = models.GenericIPAddressField(verbose_name='外网IP', unique=True, null=True, blank=True)
    private_ip = models.GenericIPAddressField(verbose_name='内网IP', null=True, blank=True)
    vpn_ip = models.GenericIPAddressField(verbose_name='VPN', null=True, blank=True)
    os = models.CharField(max_length=128, verbose_name='系统版本', null=True, blank=True)
    cpu = models.CharField(max_length=64, verbose_name='CPU', null=True, blank=True)
    memory = models.CharField(max_length=64, verbose_name='内存', null=True, blank=True)
    disk = models.CharField(max_length=256, verbose_name="硬盘", null=True, blank=True)
    bandwidth = models.IntegerField(verbose_name='外网带宽', null=True, blank=True, default="1")
    status = models.SmallIntegerField(choices=machine_status, default=0, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间', blank=True)
    last_update = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间', blank=True)
    expire_time = models.DateTimeField(auto_now=True, null=True, verbose_name='过期时间', blank=True)
    memo = models.CharField(max_length=1024, verbose_name="备注", null=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='管理员')
    platform = models.OneToOneField(CloudManufacturer, on_delete=models.CASCADE, verbose_name='平台')
    region = models.OneToOneField(IDCRegion, on_delete=models.CASCADE, verbose_name='区域')

    def __str__(self):
        return self.hostname


