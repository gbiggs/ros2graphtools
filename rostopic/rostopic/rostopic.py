#!/usr/bin/env python3

"""rostopic tool.

Command-line tool for introspecting ROS topics from a shell.
"""

import argparse


def main():
    """Main entry point for rostopic command."""
    p = argparse.ArgumentParser(description='ROS topic introspection tool')
    p.add_argument('command', help='the command to execute')
    args = p.parse_args()
    print('/topic1\n/topic2\n')
    return 0
