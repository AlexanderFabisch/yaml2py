#!/usr/bin/env python


from distutils.core import setup
import yaml2py


if __name__ == "__main__":
    setup(name='yaml2py',
          version=yaml2py.__version__,
          author='AUTHOR',
          author_email='AUTHOR EMAIL',
          maintainer='MAINTAINER',
          maintainer_email='MAINTAINER EMAIL',
          url='URL',
          description='DESCRIPTION',
          long_description=open('README.rst').read(),
          packages=['yaml2py'],)
