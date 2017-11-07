# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (
        ListView,
        DetailView,
        View,
        TemplateView
    )


from pdfview.views import PDFViewMixin

# Create your views here.
from django.http import HttpResponse
from workers.models import Worker
from django.template.loader import get_template
from django.template import RequestContext


class Index(TemplateView):
    template_name = 'index.html'


class WorkerList(ListView):
    model = Worker
    template_name = 'worker_list.html'


class WorkerView(DetailView):
    model = Worker
    template_name = 'worker_detail.html'


class PagePDFView(PDFViewMixin, DetailView):
    model = Worker
    template_name = 'pdf_view.html'

# class GeneratePDF(PDF):
#
#     model = Worker
#
#     def get_context_data(self, **kwargs):
#         context = super(WorkerView, self).get_context_data(**kwargs)
#         return context
#
#     def get(self, request, *args, **kwargs):
#         template = get_template('pdf_view.html')
#         context = {}
#         pdf = render_to_pdf('pdf_view.html', context)
#         return HttpResponse(pdf, content_type='application/pdf')


#
# def worker_list(request):
#     workers = Worker.objects.all()
#     contexto = {'workers':workers}
#     return render(request, 'worker_list.html', contexto)
