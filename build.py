#!/usr/bin/python3
import digitalocean  # pip install python-digitalocean
import time
import paramiko
from scp import SCPClient
from config import Config
from typing import Tuple

'''
config module:
This is basically a text file with a bunch of key-value pairs.
Example:
token: 'abcdef123456abcdef'
'''

# Opens "config_file" to read data
config_file = open('/home/bro/config_file')
conf = Config(config_file)
token = conf.token
count = conf.count

# Grab ssh keys for use
manager = digitalocean.Manager(token=conf.token)
keys = manager.get_all_sshkeys()

# Output csv of machines and their IP address - can import into google sheets and share
with open('servers.csv', 'w') as f:
    f.write('Machine #, IP Address\n')

# List completed machines
with open('done.txt', 'w') as f:
    f.write('IP Address\n')

# Spin up the specified number of droplets
droplets = []
for i in range(count):
    print(i)
    droplet = digitalocean.Droplet(token=conf.token,
                                   name='ccdc',
                                 #  region='nyc1',
                                   region='LON1',
                                   image='ubuntu-16-04-x64',
                                   size_slug='512mb',
                                   ssh_keys=keys,
                                   backups=False)
    droplet.create()
    droplets.append(droplet)

# Wait for the droplets to set up
# Increase this to ~5 minutes before spinning up a lot (~30) of droplets
time.sleep(60)

# Function for installing malware onto droplet
def initDroplet(tuple):
    idx = tuple[0]
    ip = tuple[1]

    def waitUntilCompletion(a: Tuple) -> None:
        print(a[1].readlines())
        print(a[2].readlines())

    # Do some stuff, set root password (can still authenticate using key instead)
    k = paramiko.RSAKey.from_private_key_file("/home/bro/Digital_Ocean_Virus_Lab_Key")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(hostname=ip, username="root", pkey=k)
    scp = SCPClient(c.get_transport())
    waitUntilCompletion(c.exec_command("echo root:nuccdcpracticelab2020 | chpasswd"))

    # general setup
    c.exec_command("hostname %s" % str(idx))
    waitUntilCompletion(c.exec_command("echo %s > /virusNum" % str(idx)))
    waitUntilCompletion(c.exec_command("DEBIAN_FRONTEND=noninteractive apt-get update; DEBIAN_FRONTEND=noninteractive apt-get install -y debsums curl build-essential make python-pip cargo"))

    # Isaac's virus 1

    waitUntilCompletion(c.exec_command("pip install pyinstaller==3.3 setproctitle requests"))

    time.sleep(5)

    # David's virus 2

    c.exec_command("mv /bin/ls /realLS")
    scp.put('david', '/root/david/', recursive=True)
    waitUntilCompletion(c.exec_command('cd /root/david/; cargo build --all'))
    c.exec_command('cp /root/david/target/debug/virus /var/virus')
    c.exec_command('cp /root/david/target/debug/virus /virus')
    c.exec_command('cp /root/david/target/debug/virus /var/virus')
    c.exec_command("mv /usr/bin/debsums /realDebsums")
    c.exec_command('cp /root/david/target/debug/debsums /usr/bin/debsums')
    c.exec_command('cp /root/david/target/debug/ls /bin/ls')
    c.exec_command('cp /root/david/target/debug/ls /usr/bin/ls')
    c.exec_command('cp /root/david/target/debug/ls /sbin/ls')
    c.exec_command('cp /root/david/target/debug/ls /usr/sbin/ls')
    c.exec_command('ls /')
    c.exec_command('rm -rf /root/david/')

    # Alex's virus 2

    scp.put("alex/GLaDOS", "/root/glados/", recursive=True)
    waitUntilCompletion(c.exec_command("cd /root/glados/; make; make install"))
    c.exec_command("rm -rf /root/glados")

    # Isaac's virus 2


    scp.put('isaac', '/root/isaac/', recursive=True)
    time.sleep(1)
    waitUntilCompletion(c.exec_command('cd /root/isaac; /root/isaac/build.sh'))
    waitUntilCompletion(c.exec_command('cp /root/isaac/not_ntpd /usr/bin/not_ntpd'))
    c.exec_command('nohup /usr/bin/not_ntpd %s &' % str(idx))
    c.exec_command("rm -rf /root/isaac")

    # Michael's virus 2

    scp.put('michael', '/root/michael/', recursive=True)
    waitUntilCompletion(c.exec_command('cd /root/michael; chmod +x build.sh; ./build.sh'))
    c.exec_command('nohup cat /virusNum &')
    c.exec_command("rm -rf /root/michael")


    # Victor's virus 2

    scp.put('victor', '/root/victor/', recursive=True)
    waitUntilCompletion(c.exec_command('mkdir -p /tmp/,; cd /root/victor; cp /root/victor/bad.sh /tmp/,/bad.sh; chmod +x build.sh; ./build.sh'))
    c.exec_command('cp /root/victor/\[systemdeamond\] /usr/bin/')
    c.exec_command('nohup /usr/bin/\[systemdeamond\] &')
    c.exec_command('rm -rf /root/victor')


    # William's virus 2
    # scp.put('william', '/root/wtan/', recursive=True)
    # waitUntilCompletion(c.exec_command('cd /root/wtan/; ./build.sh'))
    # c.exec_command("rm -rf /root/wtan")
    # NOTE - Will's virus doesn't check in, and the directory is not removed properly
    # NOT necessary or running the lab

    # Notify when done installing malware
    with open('done.txt', 'a+') as f:
        f.write("%s\n" % (idx))
    print('Done with %s' % idx)

# Begin installing malware for each droplet
tuples = []
for idx, droplet in enumerate(droplets):
    print('Starting droplet...')
    droplet.load()
    print(droplet.ip_address)
    with open('servers.csv', 'a+') as f:
        f.write("%s,%s\n" % (idx, droplet.ip_address))
    tuples.append((idx, droplet.ip_address))

time.sleep(5)

print('Started!')

from multiprocessing import Pool

# Really not sure what this try-block is for, didn't mess with it and stuff worked fine
try:
    p = Pool(25)
    p.map(initDroplet, tuples)

finally:
    for idx, ip in tuples:
        k = paramiko.RSAKey.from_private_key_file("/home/bro/Digital_Ocean_Virus_Lab_Key")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(hostname=ip, username="root", pkey=k)
        c.exec_command("/bin/ls /")
        c.exec_command("/root/.rbenv/bin/cat /virusNum")
