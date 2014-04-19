#! /usr/bin/env python

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
        ],
      entry_points = {
        'console_scripts': [
            'sgg-httpd = sgg.app.httpd:main',
            ],
        },
      package_data = {'sgg': ['web/static/*']},
      )
