from __future__ import unicode_literals
from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ContactUsView

urlpatterns = [
    url(r'^$', ContactUsView.as_view(), {}, 'contactus'),
    url(r'^success/$', TemplateView.as_view(
        template_name='contactus/contact_success.html'),
        {}, 'contactus-success'),
]
