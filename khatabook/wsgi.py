import os
import sys

# assuming your Django settings file is at
# '/home/myusername/mysite/mysite/settings.py'
path = '/home/lifecare/lifecare'
if path not in sys.path:
     sys.path.insert(0, path)


os.environ['DJANGO_SETTINGS_MODULE'] = 'khatabook.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()