from django.conf.urls import url

from .views import add_to_feincms_navigation, remove_from_feincms_navigation


urlpatterns = [
    url(r'^add-to-nav/$', add_to_feincms_navigation, name='add-to-nav'),
    url(r'^remove-from-nav/$', remove_from_feincms_navigation, name='remove-from-nav'),
]