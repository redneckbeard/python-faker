import os
from distutils.core import setup

setup(
    name = "python-faker",
    version = "0.2.0",
    url = 'http://github.com/threadsafelabs/python-faker',
    license = 'BSD',
    description = "Generate placeholder data.",
    author = 'Jonathan Lukens',
    author_email = 'jonathan@threadsafelabs.com',
    packages = ['faker', 'faker.templatetags'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
