# coding : utf-8
from django.db import models
import django.utils.timezone as timezone
# Create your models here.
class t_ip(models.Model):
    ip = models.CharField(max_length=15)
    port=models.IntegerField()
    created = models.DateTimeField('保存日期',default = timezone.now)
    updated = models.DateTimeField('最后修改日期', auto_now = True)