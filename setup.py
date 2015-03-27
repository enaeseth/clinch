#!/usr/bin/env python3

import os.path
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

root = os.path.abspath(os.path.dirname(__file__))

def read_requirements(filename):
    path = os.path.join(root, filename)
    with open(path, 'rt') as f:
        return [line.strip() for line in f]

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

    tests_require=read_requirements('dev-requirements.txt'),
    cmdclass={'test': PyTest},
)
