from __future__ import absolute_import, unicode_literals

from django import forms
from django.db import models
from django.utils.safestring import mark_safe

from feincms.module.page.forms import PageAdminForm
from feincms import extensions
from feincms.module.page.models import Page
from mptt.fields import TreeManyToManyField


class Extension(extensions.Extension):
    def handle_model(self):
        self.model.add_to_class('feincms_navigation', TreeManyToManyField(Page, blank=True, symmetrical=False, help_text='Pages linked to in the navigation of this page.', limit_choices_to={'in_navigation': True}, related_name='fein_nav'))

    def handle_modeladmin(self, modeladmin):
        modeladmin.add_extension_options('feincms_navigation')
