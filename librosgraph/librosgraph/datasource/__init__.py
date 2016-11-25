"""Data sources for information about topics, services, etc."""


def DummyTopicSource():
    """Lazy import for the DummyTopicSource class."""
    from .dummy_topic_source import DummyTopicSource
    return DummyTopicSource()
