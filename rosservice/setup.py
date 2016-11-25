"""rosservice command-line tool setup file."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='rosservice',
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
    description='Command line tool for working with ROS services.',
    long_description=(
        'A tool for introspecting and working with ROS services '
        'from the command line.'),
    license='Apache License, Version 2.0',
    test_suite='test',
)
