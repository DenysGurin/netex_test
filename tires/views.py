from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tire


class TiresList(ListView):

    model = Tire
    

class TiresDetail(DetailView):

    model = Tire
       
        
class TiresCreate(CreateView):

    model = Tire
    fields = []
    success_url = reverse_lazy('tire-list')


class TiresUpdate(UpdateView):

    model = Tire
    fields = '__all__'
    template_name_suffix = '_update_form'


class TiresDelete(DeleteView):

    model = Tire
    success_url = reverse_lazy('tire-list')
