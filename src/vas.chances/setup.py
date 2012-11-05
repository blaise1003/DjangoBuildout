from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='vas.chances',
      version=version,
      description="VAS Chances Project",
      long_description="""VAS Chances Project""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Biagio Grimaldi',
      author_email='biagio.grimaldi@gmail.com',
      url='',
      license = 'BSD',
      packages = find_packages(),
      namespace_packages = ['vas'],
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires = [
            'distribute',
            'Django'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
