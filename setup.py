#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import sys
from os import path

name = 'gcp'

setup(name=name,
      version='0.1.4',
      description=u"gcp is an advanced copy tool loosely inspired from cp",
      long_description=u'gcp is a command-line tool to copy files, loosely inspired from cp, but with high level functionalities such as progress bar, copy continuation on error, journaling to know which files were successfuly copied, name mangling to workaround filesystem limitations (FAT), unique copy queue, copy list managemet, command arguments close to cp',
      author='Goffi (Jérôme Poisson)',
      author_email='goffi@goffi.org',
      url='http://wiki.goffi.org/wiki/Gcp',
      classifiers=['Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   'Topic :: Utilities'
                   ],
      data_files=[('share/locale/fr/LC_MESSAGES', ['i18n/fr/LC_MESSAGES/gcp.mo']),
                  ('share/man/man1', ["gcp.1"]),
                  ('share/doc/%s' % name, ['COPYING','README.md'])],
      scripts=['gcp'],
     )
