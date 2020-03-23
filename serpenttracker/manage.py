#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "serpenttracker.settings")

    # MyProject Customization: run coverage.py around tests automatically
    running_tests = sys.argv[1] == "test"
    if running_tests:
        from coverage import Coverage

        cov = Coverage()
        cov.erase()
        cov.start()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    if running_tests:
        cov.stop()
        cov.save()
        covered = cov.report()
        if covered < 100:
            sys.exit(1)
