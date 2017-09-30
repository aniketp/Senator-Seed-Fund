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
    url(r'^open_ssf/$', views.open_ssf_list, name='open_ssf'),

    # Force closing
    url(r'close_ssf/$', views.force_closing, name='close_ssf'),

    # Open for funding
    url(r'^start_ssf_funding/$', views.open_for_funding, name='start_ssf_funding'),

    # Send to Kunal
    url(r'^send_to_chair/$', views.send_to_chair, name='send_to_chair'),

    # Add senators
    url(r'^add_senator/$', views.add_senator, name='add_senator'),

    # Send to Baap
    url(r'^send_to_parent/$', views.send_to_parent, name='send_to_parent'),
]