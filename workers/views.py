# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView,
        View
    )

from .utils import render_to_pdf

# Create your views here.
from django.http import HttpResponse
from workers.models import Worker
from django.template.loader import get_template

class WorkerList(ListView):
    model = Worker
    template_name = 'worker_list.html'

class WorkerView(DetailView):
    model = Worker
    template_name = 'worker_detail.html'

class GeneratePDF(View):
    model = Worker
    def get(self, request, *args, **kwargs):
        template = get_template('pdf_view.html')
        contexto = {}
        pdf = render_to_pdf('pdf_view.html', contexto)
        return HttpResponse(pdf, content_type='application/pdf')


#
# def worker_list(request):
#     workers = Worker.objects.all()
#     contexto = {'workers':workers}
#     return render(request, 'worker_list.html', contexto)
