import os
from paste.deploy import loadapp

os.system("python setup.py develop")
path = os.getcwd()
application = loadapp('config:appfog.ini', relative_to=path)
