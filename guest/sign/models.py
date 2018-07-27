# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)  #发布会标题
    limit = models.IntegerField()            #参加人数
    status = models.BooleanField()           #状态
    address = models.CharField(max_length=200)         #地址
    start_time = models.DateTimeField('events time')   #发布会时间
    create_time = models.DateTimeField(auto_now=True)  #创建时间（自动获取当前时间）
    def _str_(self):
        return self.name

#嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event)
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("event","phone")

    def _str_(self):
        return self.realname