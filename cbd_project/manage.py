#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    # Add path to this folder to python path
    sys.path.append(os.path.abspath(os.path.join(__file__, os.pardir)))
    # Settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cbd_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
