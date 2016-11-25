#!/usr/bin/env python3

"""Test the 'rostopic list' command."""

import io
import unittest
from unittest.mock import patch

import rostopic


class TestListTopics(unittest.TestCase):
    """Test topic listing functionality."""

    def test_list_all_topics(self):
        """Test listing all topics: 'rostopic list'."""
        expected_topic_list = 'topic1\ntopic2\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rostopic.list(datasource=rostopic.datasource.DummyTopicSource)
            self.assertEqual(fake_stdout.getvalue(), expected_topic_list)


if __name__ == '__main__':
    unittest.main()
