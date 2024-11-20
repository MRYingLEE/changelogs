#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests>=2.26.0',
    'validators>=0.18.2',
    'packaging>=21.3',
    'lxml>=4.6.3',
    'gitchangelog>=3.0.4'
]

test_requirements = [
    'mock>=4.0.3',
    'pytest>=6.2.5',
    'pytest-cov>=2.12.1',
    'betamax>=0.8.1',
    'betamax-serializers>=0.2.0'
]

dev_requirements = test_requirements + [
    'flake8>=3.9.2',
    'tox>=3.24.4',
]

extras_requirements = {
    'test': test_requirements,
    'dev': dev_requirements,
}

setup(
    name='changelogs',
    version='0.15.1-dev',
    description="A changelog finder and parser.",
    long_description_content_type='text/x-rst',
    long_description=readme + '\n\n' + history,
    author="pyup.io",
    author_email='support@pyup.io',
    url='https://github.com/pyupio/changelogs',
    packages=[
        'changelogs',
    ],
    package_dir={'changelogs':
                 'changelogs'},
    entry_points={
        'console_scripts': [
            'changelogs=changelogs.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='changelogs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    extras_require=extras_requirements,
)
