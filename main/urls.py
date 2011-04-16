#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from views import feed, user, page
import cron, tool

urlpatterns = patterns('',
    # 管理feed的添加、订阅
    (r'^feed/$', feed.list),
    (r'^feed/add/$', feed.add),
    (r'^feed/love/$', feed.list_love),
    (r'^feed/love/(\d+)/$', feed.add_love),
    (r'^feed/hate/(\d+)/$', feed.del_love),


    # 展示用户主界面
    (r'^user/$', user.list),
    (r'^user/add/$', user.add),
    (r'^user/(\w+)/$', user.view),
    (r'^user/(\w+)/recipe/$', user.download_recipe),
    (r'^user/(\w+)/readnow/$', user.read_now),

    # 用于定时任务
    (r'^cron/next_user/$', cron.next_user),

    # 用于外部系统支持
    (r'tool/build_recipe/$', tool.build_recipe),

    # 基本页面
    (r'^/?$', page.index),
    #(r'^.*$', page.page404),
)

