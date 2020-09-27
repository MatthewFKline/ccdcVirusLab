# CCDC Virus Lab

_build.py_ contains the code for building the digitalocean droplets and deploying the viruses on them. 

_down.py_ destroys all of the created digitalocean droplets. 

_index.html_ and _server.py_ are the monitoring webserver (_server.py_ also relies on redis).

_deploy_scoreboard_droplet.py_ makes a digitalocean droplet and places the scoreboard server files on it.

_provision_scoreboard_droplet_ sets up the scoreboard (should be run on the droplet created with _deploy_scoreboard_droplet.py_)

_update_scoreboard_address_ rewrites the hardcoded IP addresses in each virus (NOTE: Need to a regex in this, currently relies on a non-sustainable placeholder)

_virus.py_ is an example virus.

All the directories contain each individual's virus.


## Lab

For this lab, the team wrote various pieces of malware and ran them on virtual servers. Participants were tasked with removing the malware. All **viruses** call out to the monitoring interface (currently hardcoded), allowing participants to track their progress.

## Notes

DigitalOcean will cap your maximum number of droplets (either 5 or 10, don't recall).  To raise this number, you need to submit a ticket for increasing the droplet cap.
</br>
</br>
Make sure you point the viruses towards your monitoring server.  I.e. spin up the monitoring server first, then edit the IP's in the virus' before running "build.py" to point to the monitoring server.
</br>
</br>
TODO: Elaborate
