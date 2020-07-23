# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from campanas_publicitarias import views


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    path('campanas/', views.campanas, name='campanas'),
    path('campanas/create/', views.campanas_create, name='campanas_create'),
]
