# CCDC Virus Lab

build.py contains the code for building the digitalocean droplets. 

down.py destroys all of the created digitalocean droplets. 

index.html and server.py are the monitoring webserver (server.py also relies on redis).

virus.py is an example virus.

All the directories contain each individual's virus.


## Lab

For this lab, the team wrote various pieces of malware and ran them on virtual servers. Participants were tasked with removing the malware. All **viruses** call out to the monitoring interface (currently hardcoded), allowing participants to track their progress.

## Notes

DigitalOcean will cap your maximum number of droplets (either 5 or 10, don't recall).  To raise this number, you need to submit a ticket for increasing the droplet cap.
</br>
</br>
Make sure you point the viruses towards your monitoring server.  I.e. spin up the monitoring server first, then edit the IP's in the virus' before running "build.py" to point to the monitoring server.
