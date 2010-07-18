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

If you are a Django developer, you might also be interested in django-poseur, which provides some higher-level tools for Django built on this library.
