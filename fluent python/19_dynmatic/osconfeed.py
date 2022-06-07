# -*- coding: utf-8 -*-
from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://localhost/html/osconfeed.json'
JSON = 'data/osconfeed.json'

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL,JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON,'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)
