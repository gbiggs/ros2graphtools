"""Tests for the rostopic command line tool."""

import os
import sys

assert 'rostopic' not in sys.modules, 'rostopic should not have been imported before running tests'
sys.path.insert(0, os.getcwd())

import rostopic  # noqa
assert rostopic
