#!/usr/bin/env python

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pierre/GestPEA/Python/')
from main import app as application
application.secret_key = 'gestPEA'