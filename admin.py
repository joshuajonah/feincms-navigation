from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def add_to_navigation(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("%s?ct=%s&ids=%s&next=%s" % (
    	reverse('add-to-nav'), 
    	ct.pk, 
    	",".join(selected),
    	request.path
    ))
add_to_navigation.short_description = "Add items to navigation"


def remove_from_navigation(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("%s?ct=%s&ids=%s&next=%s" % (
    	reverse('remove-from-nav'), 
    	ct.pk, 
    	",".join(selected),
    	request.path
    ))
remove_from_navigation.short_description = "Remove items from navigation"