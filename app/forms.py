from django.forms import ModelForm
from .models import *

class campana_publicitariaForm(ModelForm):
    class Meta():
        model = campana_publicitaria
        fields = '__all__'

class empresaForm(ModelForm):
    class Meta():
        model = empresa
        fields = '__all__'