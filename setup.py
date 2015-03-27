#!/usr/bin/env python3

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        exit_status = pytest.main(self.pytest_args)
        sys.exit(exit_status)

setup(
    name='clinch',
    version='0.0.1',
    packages=find_packages(),

    tests_require=[
        'pytest>=2.7.0,<3',
        'pytest-cov>=1.8.1,<2',
    ],
    cmdclass={'test': PyTest},
)
