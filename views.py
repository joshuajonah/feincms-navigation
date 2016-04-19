from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ModifyFeincmsNavigation


# django 1.6, 1.5 and 1.4 supports
try:
    atomic_decorator = transaction.atomic
except AttributeError:
    atomic_decorator = transaction.commit_on_success


@staff_member_required
def add_to_feincms_navigation(request):

    @atomic_decorator
    def add_to_nav(queryset, value):
        for item in queryset:
            item.feincms_navigation.add(*value)
            item.save()

    ct = ContentType.objects.get(pk=request.GET.get('ct'))
    ct_model = ct.model_class()
    queryset = ct_model.objects.filter(pk__in=request.GET.get('ids').split(','))
    data = request.POST if request.POST else None
    form = ModifyFeincmsNavigation(data)
    if request.method == 'POST':
        if form.is_valid():
            add_to_nav(queryset, form.cleaned_data['feincms_navigation'])
            return HttpResponseRedirect(request.GET.get('next'))

    context = {
        'title': 'Add Items To Navigation',
        'form': form,
        'form_url': '?%s' % request.GET.urlencode(), 
        'is_popup': False,
        'add': True,
        'change': False,
        'has_delete_permission': False,
        'has_change_permission': True,
        'has_absolute_url': False,
        'opts': ct_model._meta,
        'save_as': False,
        'show_save': True,
        'queryset': queryset
    }

    return render(request, 'admin/modify-feincms-navigation.html', context)


@staff_member_required
def remove_from_feincms_navigation(request):

    @atomic_decorator
    def remove_from_nav(queryset, value):
        for item in queryset:
            item.feincms_navigation.remove(*value)
            item.save()

    ct = ContentType.objects.get(pk=request.GET.get('ct'))
    ct_model = ct.model_class()
    queryset = ct_model.objects.filter(pk__in=request.GET.get('ids').split(','))
    data = request.POST if request.POST else None
    form = ModifyFeincmsNavigation(data)
    if request.method == 'POST':
        if form.is_valid():
            remove_from_nav(queryset, form.cleaned_data['feincms_navigation'])
            return HttpResponseRedirect(request.GET.get('next'))

    context = {
        'title': 'Remove Items From Navigation',
        'form': form,
        'form_url': '?%s' % request.GET.urlencode(), 
        'is_popup': False,
        'add': True,
        'change': False,
        'has_delete_permission': False,
        'has_change_permission': True,
        'has_absolute_url': False,
        'opts': ct_model._meta,
        'save_as': False,
        'show_save': True,
        'queryset': queryset
    }

    return render(request, 'admin/modify-feincms-navigation.html', context)