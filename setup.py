#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Olivier Poitrey <rs@dailymotion.com>

from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='gcs-oauth2-boto-env-plugin',
    version='0.1.1',
    description='Google Storage auth2 plugin with support for passing service key via environment',
    long_description=readme,
    keywords='oauth2 gcs s3 boto plugin docker',
    author='Olivier Poitrey',
    author_email='rs@dailymotion.com',
    url='https://github.com/rs/gcs-oauth2-boto-env-plugin',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    py_modules=['gcs_oauth2_boto_env_plugin'],
    install_requires=[
        'gcs_oauth2_boto_plugin>=1.8'
    ],
)
