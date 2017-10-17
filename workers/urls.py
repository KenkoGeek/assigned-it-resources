from django.conf.urls import url
from workers import views
from workers.views import (
        WorkerList,
        WorkerView
   )

urlpatterns = [
    # url(r'^workers/', include('workers.urls')),
    url(r'^list/$', WorkerList.as_view(), name='worker_list'),
    url(r'^view/(?P<pk>\d+)/$', WorkerView.as_view(), name='worker_view'),
]
