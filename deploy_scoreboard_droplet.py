#!/usr/bin/python3
import digitalocean  # pip install python-digitalocean
import time
import paramiko
from scp import SCPClient
from config import Config
from typing import Tuple
import sys

# Opens "config_file" to read data
config_file = open('/home/bro/config_file')
conf = Config(config_file)
token = conf.token
count = conf.count

# Grab ssh keys for use
manager = digitalocean.Manager(token=conf.token)
keys = manager.get_all_sshkeys()

droplet = digitalocean.Droplet(token=conf.token,
                                   name='scoreboard',
                                 #  region='nyc1',
                                   region='LON1',
                                   image='ubuntu-20-04-x64',
                                   size_slug='4gb',
                                   ssh_keys=keys,
                                   backups=False)
droplet.create()
time.sleep(90)
droplet.load()

def waitUntilCompletion(a: Tuple) -> None:
    print("=" * 80 + "\n" + "=" * 80)
    print(a[1].readlines())
    print(a[2].readlines())
    print("=" * 80 + "\n" + "=" * 80)

# Do some stuff, set root password (can still authenticate using key instead)
k = paramiko.RSAKey.from_private_key_file("/home/bro/Digital_Ocean_Virus_Lab_Key")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname=droplet.ip_address, username="root", pkey=k)
scp = SCPClient(c.get_transport())
scp.put('server.py', '/root/server.py')
scp.put('index.html', '/root/index.html')
scp.put('provision_scoreboard_droplet', '/root/provision_scoreboard_droplet')

# general setup

print("\nScoreboard droplet at {0}:8080\n".format(droplet.ip_address))

print("ssh root@{0}\n".format(droplet.ip_address))



