# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect 
from django import template
from django.contrib import messages
from django.template import RequestContext
from django.views.generic import CreateView, ListView
from django.urls import reverse
from .models import *
from .forms import *



@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def empresas(request):
    empresas_to_list = empresa.objects.all()
    return render(request, "empresas.html", {"empresas":empresas_to_list})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))
    
    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def add_camapana_publicitaria(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = campana_publicitariaForm(request.POST) # Bound form
        if form.is_valid():
            new_campana = form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect(reverse('campanas'))
    else:
        form = campana_publicitariaForm() # Unbound form

    return render(request, 'crearCampanaPublicitaria.html', {'form': form})

@login_required(login_url="/login/")
def campanas_publicitarias(request):
    campanas_publicitarias_to_list = campana_publicitaria.objects.all()
    return render(request, "campanas.html", {"campanas_publicitarias":campanas_publicitarias_to_list})

@login_required(login_url="/login/")
def add_empresas(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = empresaForm(request.POST) # Bound form
        if form.is_valid():
            new_empresa = form.save() # Guardar los datos en la base de datos
            return HttpResponseRedirect(reverse('empresas'))
    else:
        form = empresaForm() # Unbound form

    return render(request, 'crearEmpresa.html', {'form': form})
  