#! /usr/bin/env python

import os
import glob
from setuptools import setup, find_packages


setup(name='spiralgalaxygame',
      description='Spiral Galaxy Game',
      url='https://github.com/nejucomo/spiralgalaxygame',
      license='GPLv3',
      version='0.1.dev0',
      author='Nathan Wilcox',
      author_email='nejucomo@gmail.com',
      packages=find_packages(),
      install_requires=[
        'twisted >= 13.1',
        'txpostgres >= 1.2.0',
        'psycopg2 >= 2.5.2',
        ],
      entry_points = {
        'console_scripts': [
            'sgg-%s = sgg.app.%s:main' % (n.replace('_', '-'), n)
            for n in [
                os.path.basename(n)[:-3]
                for n in glob.glob('sgg/app/*.py')
                if not n.endswith('__init__.py')
                ]
            ],
        },
      package_data = {
        'sgg': [
            'web/static/*',
            'sql/*',
            ]
        },
      )
