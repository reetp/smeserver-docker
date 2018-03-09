# smeserver-docker
Koozali SME Server Docker support 

Various notes.

This sets up some of the basics for Docker on Koozali SME

Unfortunately it seems most apps/containers need a higher version of docker than is available in CentOS6/SME v9

That means you will need CentOS 7  /SME v10 and as I have a particularly aversion to the crap that is systemd, I wont be going down that road.

So this remains here as a set of notes and ideas.

The docker-io package creates the user and group 'dockerroot'

These can be used in docker-compose or elsewhere if required.


Docker is easier to manage with docker-compose installed

I have added that to the contrib rpm

/home/e-smith/files/docker/configs

I made a configs directory in there to store .env, `*.yml and start_stop scripts

Startup scripts for images - configs can be pulled from a docker DB

so you could do kind of

start docker-myimage

Which would run a script, pull the image settings and then start the container (may need httpd regenerated for the proxy)


So this:

docker run -d -p 127.0.0.1:80:5000 training/webapp python app.py

gets reduced to

start docker-training app

DB something like this:

db docker show

training=docker
  host=127.0.0.1
  hostMachinePort=80
  dockerContainerPort=5000
  


It should have a subdomain to run for the web proxy something like this:

db domains show

docker.somedomain.com=domain
    Content=Primary
    Description=Docker Server
    Nameservers=localhost
    TemplatePath=ProxyPassVirtualDocker
    letsencryptSSLcert=enabled



This is normally set in domains but really needs created from the the docker db

ProxyPassTarget=http://127.0.0.1:3000/



docker-compose (added by contrib)

Highest version of docker-compose that will match CentOS 6 docker 1.7.1 is v.1.5.2

$dockerComposeVersion

curl -L https://github.com/docker/compose/releases/download/$dockerComposeVersion/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose

curl -L https://github.com/docker/compose/releases/download/1.5.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose