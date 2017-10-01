from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # List of Senators
    url(r'^senatorlist/$', views.senator_list, name='senatorlist'),

    # Add SSF Form
    url(r'^add/$', views.ssf_form, name='ssf_create'),

    # Edit Form
    url(r'^edit/(?P<pk>\d+)/$', views.SenateSeedFundUpdate.as_view(), name='ssf_update'),

    # Delete Form
    url(r'^delete/(?P<pk>\d+)/$', views.SenatePostDelete.as_view(), name='banish_senate'),

    # All SSFs open for donation
    url(r'^open_ssf/$', views.open_ssf_list, name='open_ssf'),

    # Force closing
    url(r'close_ssf/(?P<pk>\d+)/$', views.force_closing, name='close_ssf'),

    # Open for funding
    url(r'^start_ssf_funding/(?P<pk>\d+)/$', views.open_for_funding, name='start_ssf_funding'),

    # Send to Kunal
    url(r'^send_to_chair/(?P<pk>\d+)/$', views.send_to_chair, name='send_to_chair'),

    # Add senators
    url(r'^add_senator/$', views.add_senator, name='add_senator'),

    # Send to Baap
    url(r'^send_to_parent/(?P<pk>\d+)/$', views.send_to_parent, name='send_to_parent'),

    # Contribute Money
    url(r'^contribute/(?P<pk>\d+)/$', views.contribute_money, name='contribute_money'),

    # Show Contributers
    url(r'^contributers/(?P<pk>\d+)/$', views.show_contributers, name='show_contributers'),
]