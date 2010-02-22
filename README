Faker
=====

Faker makes fake data.  It looks like this:

    >>> import faker
    >>> faker.name.name()
    'Gregory Spinka III'
    >>> faker.internet.email()
    'jayne@miller.com'
    >>> faker.company.name()
    'Barton, Heller and Considine'
    >>> faker.address.street_address()
    '106810 Leannon Drive'

If you are a Django developer, you can access faker from templates as well.  Just add ``faker`` to your ``INSTALLED_APPS``.  You'll then be able to load the entire faker API into a context variable.

    {% load faker_tags %}
    {% get_faker %}
    <p>Phone number: {{ faker.phone_number.phone_number }}<br />
       Zip code: {{ faker.address.zip_code }}
    </p>
