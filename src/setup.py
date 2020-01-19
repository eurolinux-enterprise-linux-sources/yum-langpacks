#!/usr/bin/env python
"""
Build script for yum-langpacks
"""
from setuptools import setup, find_packages

setup (name = "yum-langpacks",
    version = '0.4.2',
    packages = find_packages(), 
    description = "Automatic installation of langpacks of packages being installed.",
    author = 'Bill Nottingham',
    author_email = 'notting@redhat.com',
    license = 'GPLv2+',
    platforms=["Linux"],

    data_files=[('/usr/lib/yum-plugins/', ['langpacks.py']),
                ('/etc/yum/pluginconf.d/', ['langpacks.conf'])],

    classifiers=['License :: OSI Approved ::  GNU General Public License (GPL)',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 ],
)
