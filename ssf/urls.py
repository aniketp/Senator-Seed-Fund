from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^senatorlist/$', views.senator_list, name='senatorlist'),
    url(r'^add/$', views.ssf_form, name='ssf_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.SenateSeedFundUpdate.as_view(), name='ssf_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SenatePostDelete.as_view(), name='banish_senate'),
    url(r'^admin_approvals/$', views.show_admin_approvals, name='admin_approvals'),
    url(r'^ssf_funding/$', views.show_chair_approvals, name='chair_approvals'),
]