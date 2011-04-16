#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.http import HttpResponse

def index(request):
    return HttpResponse("nice")

def help(request):
    return HttpResponse("nice")

def sitemap(request):
    return HttpResponse("nice")

def page404(request):
    return HttpResponse("404")
