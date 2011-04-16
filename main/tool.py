#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os
from main.decorators import *
from tempfile import mktemp
#from django.views.decorators.csrf import csrf_protect

EBOOK_CONVERT=u"/usr/bin/ebook-convert '%s' '%s' --output-profile kindle --cache-path /var/lib/calibre.cache &"

def build_recipe(request):
    #@csrf_protect
    @page_render
    def get(request):
        return ("tool/build_recipe.html", {})

    @json_render
    def post(request):
        content = None
        if 'content' in request.POST:
            content = request.POST['content']

        if 'recipe' in request.FILES:
            f = request.FILES['recipe']
            content = f.read()

        ret = 1000
        if content:
            name = mktemp(prefix=u'ebook-', suffix='.recipe')
            with open(name, 'wb') as f:
                f.write(content)
                f.close()
            cmd = EBOOK_CONVERT%(name, name+u'.mobi')
            #ret = os.system(cmd)
            ret = cmd
        return {'ret': ret}

    if request.method == 'POST':
        return post(request)
    else:
        return get(request)

