from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse


@login_required
def index(request):
    # my_profile = GeneralBodyMember.objects.get(user=request.user)
    ssf = SenateSeedFund.objects.filter(created_by=request.user).filter(status='in progress')
    opened_ssf = SenateSeedFund.objects.filter(released=True)
    approval_ssf = SenateSeedFund.objects.filter(approval__post_holder=request.user)
    chair_ssf = SenateSeedFund.objects.filter(chair_level=True)
    fin_level = SenateSeedFund.objects.filter(fin_convener=True)
    admins = AdminPost.objects.all()
    senators = SenatePost.objects.all()

    ssf_viewer = False
    for senator in senators:
        if request.user == senator.user:
            ssf_viewer = True
            break

    if request.user == AdminPost.objects.get(pin=3).post_holder:
        ssf_viewer = True                               # Financial Convener

    chair = False
    if request.user == AdminPost.objects.get(pin=1).post_holder:
        chair = True
        ssf_viewer = True

    gbm_user = True
    for admin in admins:
        if request.user == admin.post_holder:
            gbm_user = False

    secies = AdminPost.objects.all().exclude(pin=3)  # Exclude financial convener

    secy_access = False
    for secy in secies:
        if request.user == secy.post_holder:
            secy_access = True

    return render(request, 'index.html', context={'ssf_forms': ssf, 'opened_ssf': opened_ssf, 'chair_ssf': chair_ssf,
                                                  'gbm_user': gbm_user, 'approvals': approval_ssf, 'fin': fin_level,
                                                  'chair': chair, 'secies': secy_access, 'ssf_viewer': ssf_viewer})


@login_required
def senator_list(request):
    senators = SenatePost.objects.all()
    chair = AdminPost.objects.get(pin=1).post_holder
    form = AddSenatorForm
    if request.user == chair:
        if request.method == 'POST':
            form = AddSenatorForm(request.POST)

            if form.is_valid():
                roll = form.cleaned_data['roll_no']
                member = GeneralBodyMember.objects.get(roll_no=roll).user
                SenatePost.objects.create(user=member,
                                          session=form.cleaned_data['session'],
                                          max_fund=form.cleaned_data['max_fund'])

            return HttpResponseRedirect(reverse('senatorlist'))

        return render(request, 'senators.html', context={'senators': senators, 'form': form})

    else:
        return render(request, 'no_access.html')


@login_required
def add_senator(request):
    chair = AdminPost.objects.get(pin=1).post_holder
    if request.user == chair:
        if request.method == 'POST':
            form = AddSenatorForm(request.POST)

            if form.is_valid():
                SenatePost.objects.create(user=form.cleaned_data['username'],
                                          session=form.cleaned_data['session'],
                                          max_fund=form.cleaned_data['max_fund'])

            return HttpResponseRedirect(reverse('senatorlist'))

    else:
        return render(request, 'no_access.html')


class SenatePostDelete(DeleteView):
    model = SenatePost
    success_url = reverse_lazy('senatorlist')


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
    chair = AdminPost.objects.get(pin=1)                    # Chairperson
    psg = AdminPost.objects.get(pin=2)                      # President
    snt = AdminPost.objects.get(pin=4)                      # SnTSecy
    cult = AdminPost.objects.get(pin=5)                     # Cultsecy
    sports = AdminPost.objects.get(pin=6)                   # Sportssecy

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

    ssf.status = 'sent to parent'
    ssf.save()
    return HttpResponseRedirect(reverse('index'))


@login_required
def send_to_chair(request, pk):
    ssf = SenateSeedFund.objects.get(pk=pk)
    ssf.chair_level = True
    ssf.approval.clear()
    ssf.save()

    return HttpResponseRedirect(reverse('index'))


@login_required
def open_for_funding(request, pk):
    ssf = SenateSeedFund.objects.get(pk=pk)
    ssf.status = 'approval ongoing'
    ssf.chair_level = False
    ssf.released = True
    ssf.save()

    return HttpResponseRedirect(reverse('index'))


@login_required
def open_ssf_list(request):
    funds = SenateSeedFund.objects.filter(released=True)  # TODO : Check Deadline
    senators = SenatePost.objects.all()
    form = ContributeFundForm

    chairperson = False
    if request.user == AdminPost.objects.get(pin=1).post_holder:
        chairperson = True

    fin_convener = False
    if request.user == AdminPost.objects.get(pin=3).post_holder:
        fin_convener = True

    sen_access = False
    for senator in senators:
        if request.user == senator.user:
            sen_access = True
            return render(request, 'open_for_funding.html', context={'funds': funds, 'access': sen_access,
                                                                     'form': form, 'fin': fin_convener,
                                                                     'chair': chairperson})

    return render(request, 'open_for_funding.html', context={'funds': funds, 'access': sen_access, 'form': form,
                                                             'fin': fin_convener, 'chair': chairperson})


@login_required
def show_contributers(request, pk):
    ssf = SenateSeedFund.objects.get(pk=pk)
    donations = Contribution.objects.filter(ssf=ssf)

    return render(request, 'contributers.html', context={'ssf': ssf, 'donations': donations})


@login_required
def contribute_money(request, pk):   # Show only to Senators
    funds = SenateSeedFund.objects.filter(released=True)
    ssf = SenateSeedFund.objects.get(pk=pk)
    senator = SenatePost.objects.get(user=request.user)
    form = ContributeFundForm

    if request.method == 'POST':
        form_ = ContributeFundForm(request.POST)

        if form_.is_valid():
            max_allowed = 0.33*senator.max_fund
            contribution = form_.cleaned_data['amount']

            if contribution > max_allowed:
                message = "You're not allowed to contribute more than 1/3rd of your maximum fund"
                return render(request, 'open_for_funding.html', context={'form': form, 'message': message,
                                                                         'funds': funds})

            elif ssf.amount_given + contribution > ssf.ssf:  # Exceeding maximum amount
                message = "Cannot exceed maximum fund!!"
                return render(request, 'open_for_funding.html', context={'form': form, 'message': message,
                                                                         'funds': funds})

            else:
                ssf.amount_given += contribution
                ssf.contributers.add(senator.user)
                Contribution.objects.create(ssf=ssf, contributer=senator.user, contribution=contribution)
                senator.max_fund -= contribution
                ssf.save()
                senator.save()

                if ssf.ssf == ssf.amount_given:
                    ssf.released = False
                    ssf.fin_convener = True
                    ssf.save()

                return HttpResponseRedirect(reverse('index'))

    return render(request, 'open_for_funding.html', context={'form': form, 'funds': funds})


# visible only to chair or financial convener
@login_required
def force_closing(request, pk):
    ssf = SenateSeedFund.objects.get(pk=pk)
    ssf.status = 'approval completed'
    ssf.released = False
    ssf.fin_convener = True
    ssf.save()

    return HttpResponseRedirect(reverse('open_ssf'))


# Rejection by anyone other than financial convener
# For fin convener ask Kunal
@login_required
def reject_ssf(request, pk):
    ssf = SenateSeedFund.objects.get(pk=pk)
    ssf.status = 'in progress'
    ssf.chair_level = False
    ssf.fin_convener = False
    ssf.released = False
    ssf.save()

    return HttpResponseRedirect(reverse('index'))