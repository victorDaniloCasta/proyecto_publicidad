# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("app.urls")),
]
