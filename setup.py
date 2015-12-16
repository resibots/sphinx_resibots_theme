# -*- coding: utf-8 -*-
"""`sphinx_resibots_theme` lives on `Github`_.

.. _github: https://www.github.com/resibots/sphinx_resibots_theme

Original version

.. _github: https://www.github.com/snide/sphinx_resibots_theme

"""
from setuptools import setup
from sphinx_resibots_theme import __version__


setup(
    name='sphinx_resibots_theme',
    version=__version__,
    url='https://github.com/snide/sphinx_resibots_theme/',
    license='MIT',
    author='Dave Snider',
    author_email='dave.snider@gmail.com',
    description='ReadTheDocs.org theme for Sphinx, 2013 version.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx_resibots_theme'],
    package_data={'sphinx_resibots_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
