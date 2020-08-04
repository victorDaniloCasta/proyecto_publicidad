from django.forms import ModelForm
from django.db import models
from django import forms
from .models import *

class campana_publicitariaForm(ModelForm):
    class Meta():
        model = campana_publicitaria
        fields = ('nombre_campana', 'descripcion_campana', 'objetivo_campana', 'publico_campana','ubicacion_campana', 'presupuesto_campana', 'eficacia_camapana', 'empresa_campana', 'usuario_campana')

class empresaForm(ModelForm): 
    class Meta():
        model = empresa
        fields = ('nit_empresa', 'nombre_empresa', 'estado_empresa', 'grupo')
        
                
class red_socialForm(ModelForm): 
    class Meta():
        model = red_social
        fields = ('nombre_red_social','usuario_red_social','fecha_inicio_red_social','fecha_final_red_social','cantidad_seguidores_red_social', 'cantidad_likes_red_social','cantidad_reacciones_red_social','empresa_red_social','campana_publicitaria_red_social')

class ubicacionForm(ModelForm): 
    class Meta():
        model = ubicacion
        fields = ( 'nombre_ubicacion','red_social_ubicacion')



class hashtagForm(ModelForm): 
    class Meta():
        model = hashtag
        fields = ('nombre_hastag','red_social_hashtag')
