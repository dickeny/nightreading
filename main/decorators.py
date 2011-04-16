#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response

def method(method_list):
    def deco(view):
        def func(request, *args):
            if request.method not in method_list:
                return HttpResponse("method fail")
        return func
    return deco

def page_render(view):
    def func(request, *arg):
        (tpl, ret) = view(request, *arg)
        return render_to_response(tpl, ret)
    return func

def json_render(view):
    def func(request, *arg):
        pydata = view(request, *arg)
        json = simplejson.dumps(pydata, ensure_ascii=False)
        return HttpResponse(json)
    return func

def valid_user(view):
    def func(request, user, *arg):
        # valid user
        return view(request, user, *arg)
    return func

def mix_render(view):
    def func(request, *arg):
        ret = view(request, *arg)
        if isinstance(ret, tuple):
            return render_to_response(ret[0], ret[1])
        else:
            json = simplejson.dumps(pydata, ensure_ascii=False)
            return HttpResponse(json)
    return func

