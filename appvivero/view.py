from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import LaborForm
#from django.core.urlresolvers import reverse_lazy
from .models import Procutor
from django.views.generic import CreateView

# Create your views here.
def laborview(request):

    return render(request, 'ModuloLabor/registrolabor.html')