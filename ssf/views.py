from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse


@login_required
def index(request):
    ssf = SenateSeedFund.objects.filter(created_by=request.user)

    return render(request, 'index.html', context={'ssf_forms': ssf})


@login_required
def senator_list(request):
    senators = SenatePost.objects.all()
    chair = AdminPost.objects.get(post_holder='chairperson').post_holder
    if request.user == chair:
        return render(request, 'senators.html', context={'senators': senators})

    else:
        return HttpResponseRedirect('no_access.html')


@login_required
def add_senator(request):
    chair = AdminPost.objects.get(post_holder='chairperson').post_holder
    if request.user == chair:
        if request.method == 'POST':
            form = AddSenatorForm(request.POST)

            if form.is_valid():
                SenatePost.objects.create(user=form.cleaned_data['username'],
                                          session=form.cleaned_data['session'],
                                          max_fund=form.cleaned_data['max_fund'])

            return HttpResponseRedirect(reverse('senatorlist'))

    else:
        return HttpResponseRedirect('no_access.html')


class SenatePostDelete(DeleteView):
    model = SenatePost
    success_url = reverse_lazy('senator_list')


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


@login_required
def send_to_parent(request, pk):
    ssf = SenateSeedFund.objects.get(pk=pk)
    council = ssf.council
    chair = AdminPost.objects.get(post_holder='chairperson')
    psg = AdminPost.objects.get(post_holder='president')
    snt = AdminPost.objects.get(post_holder='sntsecy')
    cult = AdminPost.objects.get(post_holder='cultsecy')
    sports = AdminPost.objects.get(post_holder='sportssecy')

    if council == 'Science & Technology Council':
        ssf.approval.add(snt)
    elif council == 'Films and Cultural Council':
        ssf.approval.add(cult)
    elif council == 'Sports Council':
        ssf.approval.add(sports)
    elif council == "Chairperson Students' Senate":
        ssf.approval.add(chair)
    elif council == 'President Student Gymkhana':
        ssf.approval.add(psg)

    return HttpResponseRedirect(reverse('index'))


@login_required
def show_admin_approvals(request):
    senate_funds = SenateSeedFund.objects.all()

    ssf_lists = []
    for fund in senate_funds:
        if request.user in fund.approval:
            ssf_lists.append(fund)

    return render(request, 'admin_approval_lists.html', context={'ssf_lists': ssf_lists})


@login_required
def send_to_chair(request, pk):
    ssf = SenateSeedFund.objects.get(pk=pk)
    ssf.chair_level = True
    ssf.approval.clear()
    ssf.save()

    return HttpResponseRedirect(reverse('admin_approvals'))


@login_required
def show_chair_approvals(request):
    chair = AdminPost.objects.get(post_holder='chairperson').post_holder
    if request.user == chair:
        ssf = SenateSeedFund.objects.filter(chair_level=True)

        return render(request, 'chair_approval_list.html', context={'ssf': ssf})

    else:
        return HttpResponseRedirect('no_access.html')


@login_required
def open_for_funding(request, pk):
    ssf = SenateSeedFund.objects.get(pk=pk)
    ssf.status = 'approval ongoing'
    ssf.save()

    return HttpResponseRedirect(reverse('chair_approvals'))


@login_required
def open_ssf_list(request):
    funds = SenateSeedFund.objects.filter(status='approval ongoing')  # TODO : Check Deadline

    return render(request, 'open_for_funding.html', context={'funds': funds})


@login_required
def contribute_money(request, pk):   # Show only to Senators
    ssf = SenateSeedFund.objects.get(pk=pk)
    senator = SenatePost.objects.get(user=request.user)
    form = ContributeFundForm

    if request.method == 'POST':
        form = ContributeFundForm(request.POST)

        if form.is_valid():
            max_allowed = 0.33*senator.max_fund
            contribution = form.cleaned_data['amount']

            if contribution > max_allowed:
                message = "You're not allowed to contribute more than 1/3rd of your maximum fund"
                return render(request, 'open_for_funding.html', context={'form': form, 'message': message})

            elif ssf.amount_given + contribution > ssf.ssf:  # Exceeding maximum amount
                message = "Cannot exceed maximum fund!!"
                return render(request, 'open_for_funding.html', context={'form': form, 'message': message})

            else:
                ssf.amount_given += contribution
                ssf.save()

                message = "Contribution successful"
                return render(request, 'open_for_funding.html', context={'form': form, 'message': message})

    return render(request, 'open_for_funding.html', context={'form': form})

# TODO : To specify who contributed what


@login_required
def force_closing(request, pk):            # visible only to chair or financial convener
    ssf = SenateSeedFund.objects.get(pk=pk)
    ssf.status = 'approval completed'
    ssf.save()

    return HttpResponseRedirect('open_for_funding.html')