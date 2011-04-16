#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.http import HttpResponse

def list(request):
    return HttpResponse("nice")

def add(request):
    return HttpResponse("nice")

def list_love(request):
    return HttpResponse("nice")

def add_love(request):
    return HttpResponse("nice")

def del_love(request):
    return HttpResponse("nice")

