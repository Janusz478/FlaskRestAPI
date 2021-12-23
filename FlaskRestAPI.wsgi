import os
import sys
path = "/var/www/FlaskRestAPI/"
if path not in sys.path:
    sys.path.append(path)
os.chdir(path)

from flaskapp import app as application
