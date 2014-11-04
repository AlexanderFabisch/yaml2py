#!/usr/bin/env python


from distutils.core import setup
import yaml2py


if __name__ == "__main__":
    setup(name='yaml2py',
          version=yaml2py.__version__,
          author='Alexander Fabisch',
          author_email='afabisch@googlemail.com',
          url='URL',
          description='Load Python objects from yaml files.',
          long_description=open('README.rst').read(),
          packages=['yaml2py'],)
