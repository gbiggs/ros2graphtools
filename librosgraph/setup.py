"""librosgraph library setup file."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='librosgraph',
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    author='Geoffrey Biggs',
    author_email='gbiggs@killbots.net',
    maintainer='Geoffrey Biggs',
    maintainer_email='gbiggs@killbots.net',
    url='https://github.com/gbiggs/ros2graphtools',
    download_url='https://github.com/gbiggs/ros2graphtools/releases',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Access information about the ROS graph.',
    long_description=(
        'A library for accessing information about the current state of the '
        'ROS graph.'),
    license='Apache License, Version 2.0',
    test_suite='test',
)
