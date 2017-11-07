from django.conf.urls import url
from workers import views
from django.contrib.auth.decorators import login_required
from workers.views import (
        WorkerList,
        WorkerView,
        PagePDFView

   )


urlpatterns = [
    # url(r'^workers/', include('workers.urls')),
    url(r'^pdf/(?P<pk>\d+)/$', login_required(PagePDFView.as_view()), name='generate_pdf'),
    url(r'^list/$', login_required(WorkerList.as_view()),name='worker_list'),
    url(r'^view/(?P<pk>\d+)/$', login_required(WorkerView.as_view()), name='worker_view'),
]
