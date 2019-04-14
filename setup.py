#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

# Requirements.
setup_requirements = ['pytest-runner'] if {'pytest', 'test', 'ptr'}.intersection(sys.argv) else []
test_requirements = ['pytest', 'pytest-pep8', 'pytest-flakes']

# Fetch readme content.
with open('docs/README.rst', 'r') as readme_file:
    readme = readme_file.read()


def main():
    setup(name='regipy',
          packages=find_packages(),
          version='1.1.1',
          description='Python Registry Parser',
          long_description=readme,
          author='Martin G. Korman',
          author_email='martin@centauri.co.il',
          url='https://github.com/mkorman90/regipy/',
          download_url='https://github.com/mkorman90/regipy/releases/download/1.0.0/regipy-1.0.0.tar.gz',
          license="MIT",
          setup_requires=setup_requirements,
          tests_require=test_requirements,
          extras_require={
              'test': test_requirements
          },
          include_package_data=True,
          keywords='Python, Python3, registry, windows registry, registry parser',
          classifiers=['Development Status :: 5 - Production/Stable',
                       'Intended Audience :: Developers',
                       'Natural Language :: English',
                       'License :: OSI Approved :: MIT License',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3.7',
                       'Topic :: Software Development :: Libraries',
                       'Topic :: Utilities'],
          entry_points={
              'console_scripts': [
                  'registry-parse-header = regipy.cli:parse_header',
                  'registry-dump = regipy.cli:hive_to_json',
                  'registry-plugins-run = regipy.cli:run_plugins',
                  'registry-plugins-list = regipy.cli:list_plugins',
                  'registry-diff = regipy.cli:reg_diff',
                  'registry-transaction-logs = regipy.cli:parse_transaction_log'
              ]
          })


if __name__ == '__main__':
    main()
