from django.conf.urls import url

from .views import TiresList, TiresDetail, TiresCreate, TiresUpdate, TiresDelete

urlpatterns = [
    url(r'^$', TiresList.as_view(), name='tire-list'),
    url(r'add/$', TiresCreate.as_view(), name='tire-add'),
    url(r'(?P<pk>[0-9]+)/$', TiresDetail.as_view(), name='tire-detail'),
    url(r'(?P<pk>[0-9]+)/edit/$', TiresUpdate.as_view(), name='tire-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', TiresDelete.as_view(), name='tire-delete'),
]