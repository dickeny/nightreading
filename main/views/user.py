#!/usr/bin/python
#-*- coding: UTF-8 -*-

from main.decorators import page_render, valid_user

@page_render
def list(request):
    return {'msg': 'nice'}

@page_render
def add(request):
    return {'msg': 'nice'}

@valid_user
@page_render
def view(request, user):
    return {'msg': 'nice'}

@valid_user
@page_render
def download_recipe(request, user):
    return {'msg': 'nice'}

@valid_user
@page_render
def read_now(request, user):
    return {'msg': 'nice'}

