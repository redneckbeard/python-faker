from setuptools import setup, find_packages

setup(
    name = "python-faker",
    version = "0.2.3",
    url = 'http://github.com/threadsafelabs/python-faker',
    license = 'BSD',
    description = "Generate placeholder data.",
    author = 'Jonathan Lukens',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
