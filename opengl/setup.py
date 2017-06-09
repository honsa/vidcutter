#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from setuptools import setup
from setuptools.extension import Extension


extensions = []
using_cython = False

if sys.platform != 'win32':
    try:
        # noinspection PyUnresolvedReferences
        from Cython.Build import cythonize
        extensions = cythonize([Extension('mpv', ['setup/mpv.pyx'], libraries=['mpv'])])
        using_cython = True
    except ImportError:
        extensions = [Extension('mpv', ['setup/mpv.c'], libraries=['mpv'])]


setup(
    name='vidcutter.demo',
    version='1.0.0',
    description='Testing Cython install options',
    long_description='i am a long description',
    author='Pete Alexandrou',
    author_email='pete@ozmartians.com',
    url='http://vidcutter.ozmartians.com',
    license='GPLv3+',
    packages=['.', 'setup'],
    setup_requires=['setuptools', 'Cython' if using_cython else ''],
    entry_points={'gui_scripts': ['vidcutter.demo = main']},
    ext_modules=extensions,
    keywords='vidcutter ffmpeg audiovideo mpv libmpv videoeditor video videoedit pyqt Qt5 multimedia',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Topic :: Multimedia :: Video :: Non-Linear Editor',
        'Programming Language :: Python :: 3 :: Only'
    ]
)
