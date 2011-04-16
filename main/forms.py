#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.froms import ModelForm
from models import User, Feed

class UserFrom(ModelForm):
    class Meta:
        model = User

class FeedForm(ModelFrom):
    class Meta:
        model = Feed

