from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^senatorlist/$', views.senator_list, name='senatorlist'),
    url(r'^add/$', views.ssf_form, name='ssf_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.SenateSeedFundUpdate.as_view(), name='ssf_update'),
]