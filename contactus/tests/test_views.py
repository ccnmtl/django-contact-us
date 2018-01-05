from django.conf import settings
from django.contrib.auth.models import AnonymousUser, User
from django.core import mail
from django.test import TestCase
from django.test.client import RequestFactory

from contactus.forms import ContactUsForm
from contactus.views import ContactUsView


class ContactUsViewTest(TestCase):

    def test_get_initial_anonymous(self):
        view = ContactUsView()
        view.request = RequestFactory().get('/contact/')
        view.request.session = {}
        view.request.user = AnonymousUser()
        initial = view.get_initial()

        self.assertFalse('name' in initial)
        self.assertFalse('email' in initial)

    def test_get_initial_not_anonymous(self):
        view = ContactUsView()
        view.request = RequestFactory().get('/contact/')
        view.request.session = {}
        view.request.user = User.objects.create(
            first_name='Foo', last_name='Bar', email='foo@bar.com')

        initial = view.get_initial()
        self.assertEquals(initial['name'], 'Foo Bar')
        self.assertEquals(initial['email'], 'foo@bar.com')

        # a subsequent call using an anonymous session returns a clean initial
        view.request.session = {}
        view.request.user = AnonymousUser()
        initial = view.get_initial()
        self.assertFalse('name' in initial)
        self.assertFalse('email' in initial)

    def test_form_valid(self):
        view = ContactUsView()
        view.request = RequestFactory().get('/contact/')
        view.request.user = AnonymousUser()

        form = ContactUsForm()
        form.cleaned_data = {
            'name': 'Foo Bar',
            'email': 'sender@ccnmtl.columbia.edu',
            'subject': 'other',
            'description': 'There is a problem'
        }

        view.form_valid(form)
        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject,
                         view.subject)
        self.assertEquals(mail.outbox[0].from_email,
                          'root@localhost')
        self.assertEquals(mail.outbox[0].to,
                          [settings.CONTACT_US_EMAIL])
