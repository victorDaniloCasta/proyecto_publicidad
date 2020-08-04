# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('empresas/', views.empresas, name='empresas'),
    path('empresas/create/', views.add_empresas, name='crearempresa'),
    path('campanas/', views.campanas_publicitarias, name='campanas_publicitarias'),
    path('campanas/create/', views.add_camapana_publicitaria, name='crearcampana'),
    path('redes/',  views.redesSociales, name='redesSociales'),
    path('redes/create/', views.add_red_social, name='crearred'),
    path('ubicacion/', views.add_ubicacion,  name='crearubicacion'),
    path('hashtag/', views.add_hashtag, name='crearhashtag'),
]
