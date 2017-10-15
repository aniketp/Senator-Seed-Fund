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
    url(r'^open-ssf/$', views.open_ssf_list, name='open_ssf'),

    # Force closing
    url(r'close-ssf/(?P<pk>\d+)/$', views.force_closing, name='close_ssf'),

    # Open for funding
    url(r'^start-ssf-funding/(?P<pk>\d+)/$', views.open_for_funding, name='start_ssf_funding'),

    # Send to Kunal
    url(r'^send-to-chair/(?P<pk>\d+)/$', views.send_to_chair, name='send_to_chair'),

    # Take back from Kunal
    url(r'^cancel-chair-request/(?P<pk>\d+)/$', views.cancel_chair_request, name='cancel_chair_request'),

    # Add senators
    url(r'^add-senator/$', views.add_senator, name='add_senator'),

    # Send to Baap
    url(r'^send-to-parent/(?P<pk>\d+)/$', views.send_to_parent, name='send_to_parent'),

    # Cancel request
    url(r'^cancel-request/(?P<pk>\d+)/$', views.cancel_request, name='cancel_request'),

    # Contribute Money
    url(r'^contribute/(?P<pk>\d+)/$', views.contribute_money, name='contribute_money'),

    # Show Contributers
    url(r'^contributers/(?P<pk>\d+)/$', views.show_contributers, name='show_contributers'),

    # Reject SSF
    url(r'reject-ssf/(?P<pk>\d+)/$', views.reject_ssf, name='reject_ssf'),

    # Final Approval List
    url(r'^final-approval-list/$', views.final_approval_list, name='final_approval_list'),

    # Rejection by Financial Convener
    url(r'^fin-reject/(?P<pk>\d+)/$', views.reject_by_fin, name='reject_by_fin'),

    # Accepted by Financial Convener
    url(r'^fin-accept/(?P<pk>\d+)/$', views.approval_by_fin, name='accept_by_fin'),
]