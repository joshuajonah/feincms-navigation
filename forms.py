from django import forms

from mptt.forms import TreeNodeMultipleChoiceField
from feincms.module.page.models import Page


class ModifyFeincmsNavigation(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('feincms_navigation', )

    def __init__(self, *args, **kwargs):
        super(ModifyFeincmsNavigation, self).__init__(*args, **kwargs)
        qs = self.fields['feincms_navigation'].queryset
        self.fields['feincms_navigation'] = TreeNodeMultipleChoiceField(queryset=qs)
        self.fields['feincms_navigation'].required = False