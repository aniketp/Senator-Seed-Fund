from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse


@login_required
def index(request):

    return render(request, 'index.html', context={})


@login_required
def senator_list(request):
    senators = SenatePost.objects.all()

    if request.user == 'chairperson':
        return render(request, 'senators.html', context={'senators': senators})

    else:
        return HttpResponseRedirect('no_access.html')


@login_required
def ssf_form(request):
    form = SenateSeedFundForm

    if request.method == 'POST':
        form = SenateSeedFundForm(request.POST)

        if form.is_valid():
            SenateSeedFund.objects.create(activity_name=form.cleaned_data['activity'],
                                          description=form.cleaned_data['description'],
                                          ssf=form.cleaned_data['ssf'],
                                          council=form.cleaned_data['council'],
                                          entity=form.cleaned_data['entity'],
                                          created_by=request.user,
                                          )

        return HttpResponseRedirect(reverse('index'))

    return render(request, 'ssf/senateseedfund_form.html', context={'form': form})


class SenateSeedFundUpdate(UpdateView):
    model = SenateSeedFund
    fields = ['activity_name', 'description', 'ssf', 'council', 'entity']
    success_url = reverse_lazy('index')