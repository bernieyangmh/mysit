__author__ = 'bernie yang'
# -*- coding:utf-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'users.views.first_page'),
    url(r'^logout/', 'users.views.user_logout'),
    url(r'^login/', 'users.views.user_login'),
    url(r'^is_login/', 'users.views.is_login'),
    url(r'^register/', 'users.views.register'),

]