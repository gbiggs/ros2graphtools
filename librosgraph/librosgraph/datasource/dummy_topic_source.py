"""Dummy topic source for use in tests."""


class DummyTopicSource:
    """Dummy topic source for use in tests."""

    def __init__(self):
        """Initialise the topic source with a fixed list of topics.

        The list of topics is:

        topic1
        topic2
        """
        self.topics = ['topic1', 'topic2']
