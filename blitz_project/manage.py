#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

sys.path.append('/Users/aleksandardaskalov/PycharmProjects/Blitz-Games-on-Django/')
import logging_setup


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blitz_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    logging_setup.setup_logging()
    main()
