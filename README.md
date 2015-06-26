[![Build Status](https://travis-ci.org/ccnmtl/django-contact-us.svg?branch=master)](https://travis-ci.org/ccnmtl/django-contact-us)

Simple, reusable "contact us" form implementation for Django.

### Installation

    $ pip install django-contact-us

Add `contactus` to `INSTALLED_APPS`.

Add a `CONTACT_US_EMAIL` setting to specify the email address that
submissions will be sent to. Obviously, you also need your Django app
to be configured properly to send email.

Add a pattern like the following to your `urls.py`:

    ('^contact/', include('contactus.urls')),

Then, in any templates, you can link to the contact page with
`{% url 'contactus' %}`.

Very likely, you will want to customize the contact page and/or
success page templates. The simplest approach is probably to copy
those files out of this repo (in `contactus/templates/contactus/`)
into the appropriate templates directory in your project and tweak.

For more flexibility in overriding options, you can also use the
`contactus.views.ContactUsView` directly in your `urls.py`.
