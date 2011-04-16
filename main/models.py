#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.db import models

class Feed(models):
    '''a feed site'''
    url = models.IntegerField(),
    title = models.CharField(),

class User(models):
    name = models.CharField(),
    email = models.EmailField(),
    feeds = models.ManyToManyField('Feed');

