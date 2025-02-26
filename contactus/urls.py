from __future__ import unicode_literals
from django.urls import path
from django.views.generic import TemplateView

from .views import ContactUsView

urlpatterns = [
    path('', ContactUsView.as_view(), {}, 'contactus'),
    path(
        'success/',
        TemplateView.as_view(
            template_name='contactus/contact_success.html'),
        {},
        'contactus-success'),
]
