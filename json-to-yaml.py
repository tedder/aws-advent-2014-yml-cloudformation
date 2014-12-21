#!/usr/bin/python

import sys
import yaml
import json

j = json.load(sys.stdin)
yaml.safe_dump(j, sys.stdout, default_flow_style=False, canonical=False)
