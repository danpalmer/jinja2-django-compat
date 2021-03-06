from os import path
from codecs import open
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='jinja2-django-compat',
    version='0.1.0',
    description='A Django compatibility library for Jinja2 templates',
    long_description=long_description,
    url='https://github.com/danpalmer/jinja2-django-compat',
    license='MIT',

    author='Dan Palmer',
    author_email='dan@danpalmer.me',

    keywords='django jinja2 tools',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(),
)
