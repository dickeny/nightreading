#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.http import HttpResponse

def next_user(request):
    return HttpResponse("nice")

