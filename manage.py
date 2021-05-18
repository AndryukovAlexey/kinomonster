#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
import time
import schedule
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kinomonster.settings")
django.setup()

# from users.views import check_prem

def main():
    # check = threading.Thread(target=thread_function)
    
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kinomonster.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # check.start()
    
    execute_from_command_line(sys.argv)


# def thread_function():
#     schedule.every().day.at("00:01").do(check_prem)
#     while True:
#         schedule.run_pending()


if __name__ == '__main__':
    
     
    main()  
    
    
