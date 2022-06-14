#!/usr/bin/env python
#### Commentaire necessaire pour dire que l'environnement est en python (sinon Apache2 est paumé)

#### Fichier qui permet de faire le lien entre le serveur Apache2 et les scripts en python
import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pierre/GestPEA/PythonApi/')
from main import app as application
#from FlaskApi_11 import app as application
#from FlaskApiSimple_11_test import app as application
application.secret_key = 'gestPEA'