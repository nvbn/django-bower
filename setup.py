from setuptools import setup, find_packages
import sys, os

version = '1'

setup(name='django-bower',
      version=version,
      description="Integrate django with bower",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'example', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'django',
          'mock',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
