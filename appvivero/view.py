from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Procutor
from django.views.generic import CreateView

def Productorview(request):
    return render(request, 'ModuloLabor/registrolabor.html')

    class Productor(CreateView):
        model = ModeloLaborVivero
        form_class = LaborForm

        def get_context_data(self, **kwargs):
            context = super(Procutor, self).get_context_data(**kwargs)
            if 'form' not in context:
                context['form'] = self.form_class(self.request.GET)
                return context

        def post(self, request, *args, **kwargs):
            self.object = self.get_object
            form = self.form_class(request.POST)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.save()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return self.render_to_response(self.get_context_data(form=form))