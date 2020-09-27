#!/usr/bin/python3

import digitalocean
from config import Config

# Opens "config_file" to read DigitalOcean token 
config_file = open('../config_file')
conf = Config(config_file)
token = conf.token

# Destroy all droplets named "ccdc"
manager = digitalocean.Manager(token=conf.token)
print([d for d in manager.get_all_droplets() if d.name == "ccdc"])
for d in manager.get_all_droplets():
    if d.name == "ccdc":
        d.destroy()
