from __future__ import unicode_literals
from django.urls import re_path
from django.views.generic import TemplateView

from .views import ContactUsView

urlpatterns = [
    re_path(r'^$', ContactUsView.as_view(), {}, 'contactus'),
    re_path(r'^success/$', TemplateView.as_view(
        template_name='contactus/contact_success.html'),
        {}, 'contactus-success'),
]
