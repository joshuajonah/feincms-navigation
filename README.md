# feincms-navigation
A FeinCMS extension allowing navigation to be customized per page. 

I found the built-in navigation module to be kind of restrictive when differnt navigation items should show up on different pages, for example in subcategories.

###Usage

1. Add `'feincms_navigation'` to your `INSTALLED_APPS` setting.

2. Add `url(r'^admin/feincms_navigation/', include('feincms_navigation.urls')),` to your project `urls.py`.

3. Run `manage.py makemigrations && manage.py migrate`. 

4. In templates you can add the navigation to your page like this:
```html
{% load feincms_tags feincms_page_tags mptt_tags %}

<ul>
  {% recursetree feincms_page.feincms_navigation.all %}
  <li>
    <a href="{{ node.get_absolute_url }}">{{ node.title }}</a>
    {% if not node.is_leaf_node %}
      <ul>
        {{ children }}          
      </ul>
    {% endif %}
  </li>
  {% endrecursetree %}
</ul>
```

There are bulk admin actions for adding and removing pages from multiple page's navigation. Adding these requires overriding your FeinCMS page module's modeladmin. Here are the steps for that:

1. Add `FEINCMS_USE_PAGE_ADMIN = False` to your `settings.py`.

2. Create or modify `<your-page-app>/admin.py` and add:

```python
from django.contrib import admin

from feincms.module.page.modeladmins import PageAdmin
from feincms_navigation.admin import add_to_navigation, remove_from_navigation

from .models import Page


class CustomPageAdmin(PageAdmin):
    actions = [add_to_navigation, remove_from_navigation]
admin.site.register(Page, CustomPageAdmin)
```
