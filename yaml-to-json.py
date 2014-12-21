#!/usr/bin/python

import sys
import yaml
import json

y = yaml.load(sys.stdin)
print json.dumps(y, indent=2)
