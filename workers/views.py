# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView,
    )

# Create your views here.
from django.http import HttpResponse
from workers.models import Worker

class WorkerList(ListView):
    model = Worker
    template_name = 'worker_list.html'

class WorkerView(DetailView):
    model = Worker
    template_name = 'worker_detail.html'
    


#
# def worker_list(request):
#     workers = Worker.objects.all()
#     contexto = {'workers':workers}
#     return render(request, 'worker_list.html', contexto)
