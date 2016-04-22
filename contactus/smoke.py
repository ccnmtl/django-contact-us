from __future__ import unicode_literals
from django.conf import settings

try:
    from smoketest import SmokeTest
except ImportError:
    # django-smoketest isn't installed
    SmokeTest = object


class ExpectedSettings(SmokeTest):
    def test_contact_us_email(self):
        self.assertIsNotNone(settings.CONTACT_US_EMAIL)
