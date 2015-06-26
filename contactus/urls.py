from django.conf.urls import patterns
from django.views.generic import TemplateView

from .views import ContactUsView

urlpatterns = patterns(
    'contactus.views',
    (r'^$', ContactUsView.as_view(), {}, 'contactus'),
    (r'^success/$',
     TemplateView.as_view(template_name='contactus/contact_success.html'),
     {}, 'contactus-success'),
)
